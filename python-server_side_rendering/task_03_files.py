"""
Flask app to display products from JSON or CSV files using query parameters.
"""

from flask import Flask, render_template, request
import json
import csv

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
    else:
        error = "Wrong source"

    if not error and id_param:
        try:
            filtered = [p for p in product_data if str(p.get('id')) == id_param]
            if not filtered:
                error = "Product not found"
            else:
                product_data = filtered
        except Exception:
            error = "Invalid data format"

    return render_template("product_display.html", products=product_data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
