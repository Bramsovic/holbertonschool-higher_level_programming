# RESTful API

## Novice Level Project  
**GitHub Repo:** `holbertonschool-higher_level_programming`  
**Directory:** `restful-api`  
**Weight:** 1  

---

## 📘 Description

This project explores the core concepts and practical applications of RESTful APIs. From understanding HTTP basics to building secure APIs with Flask, this module provides hands-on experience with both consuming and developing web services.

---

## 🎯 Learning Objectives

- Understand HTTP/HTTPS protocols and status codes
- Consume APIs using `curl` and Python
- Build simple and advanced APIs using `http.server` and Flask
- Implement authentication with Basic Auth and JWT
- Maintain API standards and documentation

---

## 💡 Why RESTful APIs Matter

REST APIs allow seamless communication between distributed systems. They are the backbone of modern web applications, enabling everything from user logins to data analytics across platforms.

---

## 📈 Project Flow Overview

```
Client --> Web Server --> API Server --> Database
  ^            |             ^               |
  |            v             |               v
Request    Process        Fetch/Modify   Return
  |            |             |               |
  +----------> + ----------> + ------------> +
  <----------- <------------ <------------- <
                Response
```

---

## ✅ Tasks Breakdown

### 0. Basics of HTTP/HTTPS

- Learn key differences between HTTP and HTTPS
- Understand HTTP request/response structure
- Explore common methods (GET, POST, PUT, DELETE)
- Learn status codes (e.g. 200, 404, 500)

### 1. Consuming APIs with `curl`

- Use `curl` to fetch content and interact with public APIs
- Test HTTP methods like `GET`, `POST`
- Practice using headers and viewing response metadata

**Examples:**
```bash
curl https://jsonplaceholder.typicode.com/posts
curl -I https://jsonplaceholder.typicode.com/posts
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### 2. Consuming APIs with Python (`requests`)

- Fetch and parse JSON data from APIs
- Print post titles and save them into a CSV file

```python
def fetch_and_print_posts():
    ...

def fetch_and_save_posts():
    ...
```

### 3. API with `http.server`

- Create a basic API using Python’s `http.server`
- Handle `/`, `/data`, `/status` routes with JSON/text responses
- Return 404 for undefined endpoints

### 4. API with Flask

- Set up a full Flask API
- Handle routes: `/`, `/status`, `/data`, `/users/<username>`
- Add `/add_user` with POST to create users in memory
- Return proper status codes (200, 201, 400)

```python
@app.route("/add_user", methods=["POST"])
def add_user():
    ...
```

### 5. API Security & Authentication

- Basic HTTP Auth with `Flask-HTTPAuth`
- JWT Auth with `Flask-JWT-Extended`
- Role-based access (`admin`, `user`)
- Handle all auth errors with consistent `401` status

**Endpoints:**

| Route           | Method | Auth Type   | Description                          |
|----------------|--------|-------------|--------------------------------------|
| `/basic-protected` | GET    | Basic Auth  | Basic authentication check           |
| `/login`           | POST   | JWT         | Login returns access token           |
| `/jwt-protected`   | GET    | JWT         | Protected with JWT                   |
| `/admin-only`      | GET    | JWT + Role  | Only accessible by `admin` users     |

---

## 📂 Project Structure

```
restful-api/
│
├── task_02_requests.py
├── task_03_http_server.py
├── task_04_flask.py
├── task_05_basic_security.py
├── main_02_requests.py
├── README.md
```

---

## 🧪 Testing

Use `curl`, browser, or Python scripts to test all endpoints. Flask server runs on `http://127.0.0.1:5000`.

```bash
curl http://127.0.0.1:5000/status
curl -H "Authorization: Bearer <token>" http://127.0.0.1:5000/jwt-protected
```



---

## 🛡️ License

This project is part of Holberton School's curriculum for educational use.
