"""
Flask app to display products from JSON, CSV,
or SQLite based on a query parameter.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_products(filepath='products.json'):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv_products(filepath='products.csv'):
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception:
        return []

def read_sql_products(db_path='products.db'):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except Exception:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    product_data = []

    if source == 'json':
        product_data = read_json_products()
    elif source == 'csv':
        product_data = read_csv_products()
    elif source == 'sql':
        product_data = read_sql_products()
    else:
        error = "Wrong source"

    if not error and id_param:
        try:
            product_data = [p for p in product_data if str(p.get('id')) == id_param]
            if not product_data:
                error = "Product not found"
        except Exception:
            error = "Invalid data format"

    return render_template("product_display.html", products=product_data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
