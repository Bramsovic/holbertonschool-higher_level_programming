# Python - Server-Side Rendering (SSR)

## 🧠 Description

This project introduces **server-side rendering (SSR)** using **Python** and **Flask**. SSR is a technique where web pages are rendered on the server and sent to the client as complete HTML, enabling faster page loads, better SEO, and improved accessibility. You'll learn how to use **Jinja templating**, read data from **JSON**, **CSV**, and **SQLite**, and build a dynamic web app that responds to user input.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

- Understand the difference between **server-side** and **client-side** rendering
- Explain the advantages of using SSR in web applications
- Implement SSR using **Flask** in Python
- Use the **Jinja2** templating engine to dynamically generate HTML pages
- Read and render data from **JSON**, **CSV**, and **SQLite**
- Handle **user input** and **dynamic content** in a Flask application

---

## 🛠️ Setup Instructions

### 1. Install Dependencies

Make sure you have **Python** installed.

Install Flask:

```bash
pip install Flask
```

---

## 📁 Project Structure

```
python-server_side_rendering/
│
├── task_00_intro.py          # Generates invitations from a text template
├── task_01_jinja.py          # Basic Flask app with HTML templates
├── task_02_logic.py          # Dynamic rendering with JSON and conditions
├── task_03_files.py          # Displays product data from JSON and CSV
├── task_04_db.py             # Extends app to handle SQLite database
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── items.html
│   ├── product_display.html
│   ├── header.html
│   └── footer.html
├── static/
│   └── (Optional CSS or JS files)
├── items.json
├── products.json
├── products.csv
└── products.db
```

---

## 🚀 Tasks Overview

### ✅ Task 0: Simple Templating Program

- Generates personalized text files (`output_X.txt`) using placeholders from a template.
- Handles missing data gracefully by inserting `"N/A"`.
- Validates input types and handles empty template/data scenarios.

### ✅ Task 1: Basic Flask App with Jinja

- Sets up a simple Flask app with routes:
  - `/` → homepage
  - `/about`
  - `/contact`
- Uses `index.html`, `about.html`, `contact.html`, with shared `header.html` and `footer.html`.

### ✅ Task 2: Dynamic Content with Jinja

- Renders `items.html` using a list from `items.json`.
- Displays all items in an unordered list.
- Shows “No items found” message if the list is empty.

### ✅ Task 3: Data Display from JSON or CSV

- Loads data from `products.json` or `products.csv` based on the query param `?source=json` or `?source=csv`.
- Optional filter by `id` via `?id=2`.
- Renders all data or a specific product using `product_display.html`.
- Displays error messages for:
  - Invalid `source`
  - Product ID not found

### ✅ Task 4: SQLite Integration

- Adds support for `source=sql` in the same route.
- Reads data from `products.db`.
- Displays data similarly in `product_display.html`.
- Handles SQL errors and invalid queries gracefully.

---

## 🧪 Testing

You can run your Flask applications like so:

```bash
python3 task_01_jinja.py
```

Then visit:

- `http://localhost:5000/`
- `http://localhost:5000/about`
- `http://localhost:5000/contact`
- `http://localhost:5000/items`
- `http://localhost:5000/products?source=json`
- `http://localhost:5000/products?source=csv`
- `http://localhost:5000/products?source=sql&id=1`

---

## 🔗 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Templating](https://jinja.palletsprojects.com/)
- [Python JSON](https://docs.python.org/3/library/json.html)
- [Python CSV](https://docs.python.org/3/library/csv.html)
- [SQLite3 in Python](https://docs.python.org/3/library/sqlite3.html)
- [MDN - Server-side Web Development](https://developer.mozilla.org/en-US/docs/Learn/Server-side)

---

## 📦 Repository

**GitHub Repository:** `holbertonschool-higher_level_programming`  
**Directory:** `python-server_side_rendering`

---

Happy Rendering! 🚀
