"""
Flask app that reads data from JSON and displays it dynamically using Jinja loops and conditions.
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template("items.html", items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
