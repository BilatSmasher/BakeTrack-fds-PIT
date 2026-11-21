# BakeBoss Flask project

## Files
- `app.py` — Flask application and page routes
- `templates/base.html` — shared layout/navigation/modal shell
- `templates/dashboard.html` — dashboard page
- `templates/credit.html` — credit page
- `templates/history.html` — transaction history page
- `templates/inventory.html` — inventory page
- `templates/sales.html` — sales / POS page
- `static/style.css` — extracted stylesheet
- `static/app.js` — shared client-side interactions and demo data

## Run locally
1. Install Python 3.9+.
2. Install Flask: `pip install flask`
3. From this folder run: `python app.py`
4. Open `http://127.0.0.1:5000`

The project keeps the original prototype's sample/demo behavior. Sales uses the original POS cart flow; History is a sample completed-transactions table.
