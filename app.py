from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
app.secret_key = "change-this-secret-key"
DB_PATH = Path(__file__).with_name("baketrack.db")


@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    with get_db() as db:
        db.executescript("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT DEFAULT 'Bread',
            price REAL NOT NULL DEFAULT 0,
            stock INTEGER NOT NULL DEFAULT 0,
            low_stock_level INTEGER NOT NULL DEFAULT 5
        );
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT DEFAULT '',
            balance REAL NOT NULL DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            sale_date TEXT NOT NULL,
            total REAL NOT NULL,
            payment_type TEXT NOT NULL,
            amount_paid REAL NOT NULL DEFAULT 0,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        );
        CREATE TABLE IF NOT EXISTS sale_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            subtotal REAL NOT NULL,
            FOREIGN KEY(sale_id) REFERENCES sales(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        );
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            payment_date TEXT NOT NULL,
            amount REAL NOT NULL,
            note TEXT DEFAULT '',
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        );
        """)
        count = db.execute("SELECT COUNT(*) FROM products").fetchone()[0]
        if count == 0:
            db.executemany(
                "INSERT INTO products(name, category, price, stock, low_stock_level) VALUES (?, ?, ?, ?, ?)",
                [
                    ("Pandesal", "Bread", 3.00, 100, 15),
                    ("Spanish Bread", "Bread", 8.00, 45, 10),
                    ("Cheese Bread", "Bread", 10.00, 35, 10),
                    ("Ensaymada", "Pastry", 18.00, 25, 8),
                    ("Loaf Bread", "Bread", 55.00, 20, 5),
                ],
            )


@app.context_processor
def inject_current_date():
    return {"current_date": datetime.now().strftime("%B %d, %Y")}


@app.template_filter("peso")
def peso(value):
    return "₱{:,.2f}".format(value or 0)


@app.route("/")
def dashboard():
    with get_db() as db:
        today = datetime.now().strftime("%Y-%m-%d")
        today_sales = db.execute(
            "SELECT COALESCE(SUM(total), 0) FROM sales WHERE substr(sale_date,1,10)=?", (today,)
        ).fetchone()[0]
        sales_count = db.execute(
            "SELECT COUNT(*) FROM sales WHERE substr(sale_date,1,10)=?", (today,)
        ).fetchone()[0]
        product_count = db.execute("SELECT COUNT(*) FROM products").fetchone()[0]
        stock_count = db.execute("SELECT COALESCE(SUM(stock),0) FROM products").fetchone()[0]
        credit_total = db.execute("SELECT COALESCE(SUM(balance),0) FROM customers").fetchone()[0]
        low_stock = db.execute(
            "SELECT * FROM products WHERE stock <= low_stock_level ORDER BY stock ASC LIMIT 6"
        ).fetchall()
        recent_sales = db.execute("""
            SELECT s.*, COALESCE(c.name, 'Walk-in Customer') AS customer_name
            FROM sales s LEFT JOIN customers c ON c.id=s.customer_id
            ORDER BY s.id DESC LIMIT 6
        """).fetchall()
    return render_template("dashboard.html", active="dashboard", today_sales=today_sales,
                           sales_count=sales_count, product_count=product_count,
                           stock_count=stock_count, credit_total=credit_total,
                           low_stock=low_stock, recent_sales=recent_sales)


@app.route("/inventory", methods=["GET", "POST"])
def inventory():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "Bread").strip()
        try:
            price = float(request.form.get("price", 0))
            stock = int(request.form.get("stock", 0))
            low_level = int(request.form.get("low_stock_level", 5))
            if not name or price < 0 or stock < 0 or low_level < 0:
                raise ValueError
        except ValueError:
            flash("Please enter a product name and valid non-negative numbers.", "error")
            return redirect(url_for("inventory"))
        with get_db() as db:
            db.execute(
                "INSERT INTO products(name,category,price,stock,low_stock_level) VALUES(?,?,?,?,?)",
                (name, category, price, stock, low_level),
            )
        flash("Product added to inventory.", "success")
        return redirect(url_for("inventory"))

    search = request.args.get("q", "").strip()
    with get_db() as db:
        if search:
            products = db.execute(
                "SELECT * FROM products WHERE name LIKE ? OR category LIKE ? ORDER BY name",
                (f"%{search}%", f"%{search}%"),
            ).fetchall()
        else:
            products = db.execute("SELECT * FROM products ORDER BY name").fetchall()
    return render_template("inventory.html", active="inventory", products=products, search=search)


@app.route("/inventory/<int:product_id>/update", methods=["POST"])
def update_product(product_id):
    try:
        price = float(request.form.get("price", 0))
        stock = int(request.form.get("stock", 0))
        low_level = int(request.form.get("low_stock_level", 5))
        if price < 0 or stock < 0 or low_level < 0:
            raise ValueError
    except ValueError:
        flash("Enter valid non-negative price and stock values.", "error")
        return redirect(url_for("inventory"))
    with get_db() as db:
        db.execute(
            "UPDATE products SET price=?, stock=?, low_stock_level=? WHERE id=?",
            (price, stock, low_level, product_id),
        )
    flash("Inventory updated.", "success")
    return redirect(url_for("inventory"))


@app.route("/sales", methods=["GET", "POST"])
def sales():
    with get_db() as db:
        if request.method == "POST":
            try:
                product_ids = request.form.getlist("product_id")
                quantities = request.form.getlist("quantity")
                customer_id = request.form.get("customer_id") or None
                payment_type = request.form.get("payment_type", "Cash")
                amount_paid = float(request.form.get("amount_paid", 0))
                if payment_type not in ("Cash", "Credit"):
                    raise ValueError
                items = []
                total = 0
                for pid, qty_text in zip(product_ids, quantities):
                    if not pid or not qty_text:
                        continue
                    qty = int(qty_text)
                    product = db.execute("SELECT * FROM products WHERE id=?", (int(pid),)).fetchone()
                    if product is None or qty <= 0 or product["stock"] < qty:
                        raise ValueError("A product is missing or has insufficient stock.")
                    subtotal = product["price"] * qty
                    total += subtotal
                    items.append((product, qty, subtotal))
                if not items:
                    raise ValueError("Add at least one product to the sale.")
                if payment_type == "Cash":
                    if amount_paid < total:
                        raise ValueError("Cash payment must cover the total amount.")
                    if customer_id:
                        customer = db.execute("SELECT id FROM customers WHERE id=?", (customer_id,)).fetchone()
                        if customer is None:
                            raise ValueError("Select a valid customer.")
                else:
                    if not customer_id:
                        raise ValueError("Select a customer for a credit sale.")
                    customer = db.execute("SELECT id FROM customers WHERE id=?", (customer_id,)).fetchone()
                    if customer is None:
                        raise ValueError("Select a valid customer.")
                    if amount_paid < 0 or amount_paid > total:
                        raise ValueError("For credit sales, amount paid must be between zero and the total.")
                cursor = db.execute(
                    "INSERT INTO sales(customer_id,sale_date,total,payment_type,amount_paid) VALUES(?,?,?,?,?)",
                    (customer_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), total, payment_type, amount_paid),
                )
                sale_id = cursor.lastrowid
                for product, qty, subtotal in items:
                    db.execute(
                        "INSERT INTO sale_items(sale_id,product_id,quantity,unit_price,subtotal) VALUES(?,?,?,?,?)",
                        (sale_id, product["id"], qty, product["price"], subtotal),
                    )
                    db.execute("UPDATE products SET stock=stock-? WHERE id=?", (qty, product["id"]))
                if payment_type == "Credit":
                    db.execute("UPDATE customers SET balance=balance+? WHERE id=?", (total - amount_paid, customer_id))
                flash(f"Sale #{sale_id} recorded successfully.", "success")
                return redirect(url_for("history"))
            except (ValueError, TypeError) as exc:
                flash(str(exc) or "Please check the sale details.", "error")
                return redirect(url_for("sales"))
        products = db.execute("SELECT * FROM products WHERE stock > 0 ORDER BY name").fetchall()
        customers = db.execute("SELECT * FROM customers ORDER BY name").fetchall()
    return render_template("sales.html", active="sales", products=products, customers=customers)


@app.route("/history")
def history():
    with get_db() as db:
        sales_rows = db.execute("""
            SELECT s.*, COALESCE(c.name, 'Walk-in Customer') AS customer_name
            FROM sales s LEFT JOIN customers c ON c.id=s.customer_id
            ORDER BY s.id DESC
        """).fetchall()
        details = {}
        for sale in sales_rows:
            details[sale["id"]] = db.execute("""
                SELECT p.name, si.quantity, si.unit_price, si.subtotal
                FROM sale_items si JOIN products p ON p.id=si.product_id
                WHERE si.sale_id=?
            """, (sale["id"],)).fetchall()
    return render_template("history.html", active="history", sales_rows=sales_rows, details=details)


@app.route("/credit", methods=["GET", "POST"])
def credit():
    with get_db() as db:
        if request.method == "POST":
            action = request.form.get("action")
            if action == "customer":
                name = request.form.get("name", "").strip()
                phone = request.form.get("phone", "").strip()
                if not name:
                    flash("Customer name is required.", "error")
                else:
                    db.execute("INSERT INTO customers(name,phone) VALUES(?,?)", (name, phone))
                    flash("Customer added.", "success")
            elif action == "payment":
                try:
                    customer_id = int(request.form.get("customer_id"))
                    amount = float(request.form.get("amount", 0))
                    note = request.form.get("note", "").strip()
                    customer = db.execute("SELECT * FROM customers WHERE id=?", (customer_id,)).fetchone()
                    if customer is None or amount <= 0 or amount > customer["balance"]:
                        raise ValueError("Enter a valid payment not exceeding the customer's balance.")
                    db.execute(
                        "INSERT INTO payments(customer_id,payment_date,amount,note) VALUES(?,?,?,?)",
                        (customer_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount, note),
                    )
                    db.execute("UPDATE customers SET balance=balance-? WHERE id=?", (amount, customer_id))
                    flash("Customer payment recorded.", "success")
                except (ValueError, TypeError):
                    flash("Please enter a valid customer and payment amount.", "error")
            return redirect(url_for("credit"))
        customers = db.execute("SELECT * FROM customers ORDER BY name").fetchall()
        payments = db.execute("""
            SELECT p.*, c.name AS customer_name FROM payments p
            JOIN customers c ON c.id=p.customer_id ORDER BY p.id DESC LIMIT 15
        """).fetchall()
        total_credit = db.execute("SELECT COALESCE(SUM(balance),0) FROM customers").fetchone()[0]
    return render_template("credit.html", active="credit", customers=customers,
                           payments=payments, total_credit=total_credit)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
