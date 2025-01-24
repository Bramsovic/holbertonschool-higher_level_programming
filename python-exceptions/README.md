
# 🐍 Python - Exceptions

This project is part of the **Holberton School Higher-Level Programming** curriculum. It focuses on **exceptions** in Python, including how to handle, raise, and manage errors effectively in your code. Through these tasks, you'll gain practical experience in making your programs more robust and error-resistant.

---

## 📋 Table of Contents

1. [📖 Description](#-description)  
2. [🎯 Learning Objectives](#-learning-objectives)  
3. [✅ Requirements](#-requirements)  
4. [📂 Repository Structure](#-repository-structure)  
5. [📚 Resources](#-resources)  
6. [🚀 How to Run](#-how-to-run)  
7. [📝 Task Overview](#-task-overview)  
   - [0. Safe list printing](#0-safe-list-printing)  
   - [1. Safe printing of an integers list](#1-safe-printing-of-an-integers-list)  
   - [2. Print and count integers](#2-print-and-count-integers)  
   - [3. Integers division with debug](#3-integers-division-with-debug)  
   - [4. Divide a list](#4-divide-a-list)  
   - [5. Raise exception](#5-raise-exception)  
   - [6. Raise a message](#6-raise-a-message)  
8. [🤝 Contribution Guidelines](#-contribution-guidelines)  
9. [👨‍💻 Author](#-author)  

---

## 📖 Description

In this project, you will learn how to manage **errors** and **exceptions** in Python. Understanding how to handle exceptions effectively is crucial for writing robust and reliable code.

The project covers:
- Catching and handling exceptions using `try` / `except`.
- Raising built-in exceptions in Python.
- Implementing cleanup actions using `finally`.
- Using exceptions to make programs resilient to invalid input or runtime issues.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

### General Concepts:
- Understand the difference between **errors** and **exceptions**.
- Know when and why to use **exceptions** in Python.
- Catch and handle exceptions properly.
- Raise built-in exceptions to indicate errors in your programs.
- Implement **cleanup actions** after exceptions using `finally`.

---

## ✅ Requirements

### Python Scripts
- **Python Version:** All files are interpreted/compiled with **Python 3.8.5** on **Ubuntu 20.04 LTS**.
- **File Format:**
  - Scripts must start with the shebang:
    ```bash
    #!/usr/bin/python3
    ```
  - Files must:
    - End with a **new line**.
    - Be **PEP 8 compliant** (`pycodestyle` version 2.7.*).
    - Be **executable**.
    - Be tested for length using the `wc` command.

### Allowed Editors:
- `vi`, `vim`, or `emacs`.

---

## 📂 Repository Structure

```plaintext
python-exceptions/
├── 0-safe_print_list.py           # Prints x elements of a list
├── 1-safe_print_integer.py        # Prints an integer
├── 2-safe_print_list_integers.py  # Prints and counts integers in a list
├── 3-safe_print_division.py       # Divides two integers with debug
├── 4-list_division.py             # Divides element by element in two lists
├── 5-raise_exception.py           # Raises a TypeError
├── 6-raise_exception_msg.py       # Raises a NameError with a message
├── README.md                      # Project documentation
```

---

## 📚 Resources

To complete this project, consult the following resources:

1. [Errors and Exceptions (Python Documentation)](https://docs.python.org/3/tutorial/errors.html)
2. [Learn to Program 11 Static & Exception Handling (YouTube)](https://www.youtube.com/watch?v=7lmCu8wz8ro)

---

## 🚀 How to Run

Follow these steps to run the scripts:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/holbertonschool-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-exceptions
   ```

3. Make the script executable:
   ```bash
   chmod +x <script_name>.py
   ```

4. Run the script:
   ```bash
   ./<script_name>.py
   ```

Alternatively, you can execute the script using Python directly:
```bash
python3 <script_name>.py
```

---

## 📝 Task Overview

### 0. Safe list printing
**File:** `0-safe_print_list.py`  
Write a function that prints `x` elements of a list, handling exceptions gracefully.
- **Prototype:** `def safe_print_list(my_list=[], x=0):`

---

### 1. Safe printing of an integers list
**File:** `1-safe_print_integer.py`  
Write a function that prints an integer using `"{:d}".format()`.
- **Prototype:** `def safe_print_integer(value):`

---

### 2. Print and count integers
**File:** `2-safe_print_list_integers.py`  
Write a function that prints and counts the integers in a list.
- **Prototype:** `def safe_print_list_integers(my_list=[], x=0):`

---

### 3. Integers division with debug
**File:** `3-safe_print_division.py`  
Write a function that divides two integers and prints the result inside a `finally` block.
- **Prototype:** `def safe_print_division(a, b):`

---

### 4. Divide a list
**File:** `4-list_division.py`  
Write a function that divides element by element two lists.
- **Prototype:** `def list_division(my_list_1, my_list_2, list_length):`

---

### 5. Raise exception
**File:** `5-raise_exception.py`  
Write a function that raises a `TypeError`.
- **Prototype:** `def raise_exception():`

---

### 6. Raise a message
**File:** `6-raise_exception_msg.py`  
Write a function that raises a `NameError` with a custom message.
- **Prototype:** `def raise_exception_msg(message=""):`

---

## 🤝 Contribution Guidelines

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature or fix"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a Pull Request with a detailed description of your changes.

---

## 👨‍💻 Author

This project is part of the **Holberton School Higher-Level Programming** curriculum.  
**Author:** [Brahim](https://github.com/Bramsovic)
```

