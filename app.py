from flask import Flask, render_template

app = Flask(__name__)

PAGES = {
    "dashboard": ("Dashboard", "dashboard.html"),
    "credit": ("Credit", "credit.html"),
    "history": ("History", "history.html"),
    "inventory": ("Inventory", "inventory.html"),
    "sales": ("Sales", "sales.html"),
}

@app.route("/")
def home():
    return render_template("dashboard.html", page="Dashboard")

@app.route("/<page>")
def show_page(page):
    page = page.lower().strip("/")
    if page not in PAGES:
        return render_template("dashboard.html", page="Dashboard")
    title, template = PAGES[page]
    return render_template(template, page=title)

if __name__ == "__main__":
    app.run(debug=True)
