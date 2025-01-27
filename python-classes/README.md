# 🐍 Python - Classes and Objects

This project is part of the **Holberton School Higher-Level Programming** curriculum. It focuses on the **fundamentals of Object-Oriented Programming (OOP)** in Python, including concepts like classes, objects, attributes, methods, and encapsulation. Through these tasks, you'll gain hands-on experience building and manipulating Python classes.

---

## 📋 Table of Contents

1. [📖 Background Context](#-background-context)  
2. [🎯 Learning Objectives](#-learning-objectives)  
3. [✅ Requirements](#-requirements)  
4. [📂 Repository Structure](#-repository-structure)  
5. [📚 Resources](#-resources)  
6. [🚀 How to Run](#-how-to-run)  
7. [📝 Task Overview](#-task-overview)  
   - [0. My first square](#0-my-first-square)  
   - [1. Square with size](#1-square-with-size)  
   - [2. Size validation](#2-size-validation)  
   - [3. Area of a square](#3-area-of-a-square)  
   - [4. Access and update private attribute](#4-access-and-update-private-attribute)  
   - [5. Printing a square](#5-printing-a-square)  
   - [6. Coordinates of a square](#6-coordinates-of-a-square)  
8. [🤝 Contribution Guidelines](#-contribution-guidelines)  
9. [👨‍💻 Author](#-author)  

---

## 📖 Background Context

It’s **VERY important** to go through all the resources provided below. Take the time to read, type (not copy-paste), and understand all the examples in the resources. Practice by experimenting with the concepts of OOP and playing with them.

This project is designed to help you **build a solid foundation in Object-Oriented Programming (OOP)**. The ultimate goal is to enable you to use OOP concepts effectively in Python and understand why Python programming is awesome.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

### General Concepts:
- Understand **Object-Oriented Programming (OOP)** and the principle of "first-class everything."
- Define and use **classes**, **objects**, and **instances** in Python.
- Explain the difference between a **class** and an **object** (or **instance**).
- Use **public**, **protected**, and **private attributes**.
- Work with the `self` keyword.
- Understand and implement **methods**, including the special `__init__` method.
- Explain **Data Abstraction**, **Encapsulation**, and **Information Hiding**.
- Differentiate between an **attribute** and a **property** in Python.
- Implement getters and setters the **Pythonic way**.
- Dynamically create new attributes for existing instances of a class.
- Bind attributes to objects and classes.
- Understand and utilize the `__dict__` attribute.
- Use the `getattr()` function to retrieve object attributes dynamically.

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

### Documentation
- **Docstrings** are **mandatory** for:
  - **Modules**: Each module must have a docstring describing its purpose.
  - **Classes**: Each class must have a docstring describing its role.
  - **Methods/Functions**: Each function or method (inside or outside a class) must have a docstring explaining its purpose and behavior.
  - Use **Google Style Python Docstrings** for documentation.

### Allowed Editors:
- `vi`, `vim`, or `emacs`.

---

## 📂 Repository Structure

```plaintext
python-classes/
├── 0-square.py         # Defines an empty class Square
├── 1-square.py         # Adds a private attribute size
├── 2-square.py         # Validates size attribute
├── 3-square.py         # Adds a method to calculate the area of the square
├── 4-square.py         # Adds getter and setter for size
├── 5-square.py         # Adds a method to print the square with #
├── 6-square.py         # Adds position attribute with validation
├── README.md           # Project documentation
```

---

## 📚 Resources

To complete this project, refer to the following resources **in order**:

1. [Object Oriented Programming (Python.org)](https://docs.python.org/3/tutorial/classes.html) (Read until the paragraph "Inheritance" excluded.)
2. [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)  
3. [Learn to Program 9: Object Oriented Programming (YouTube)](https://www.youtube.com/watch?v=1AGyBuVCTeE)  
4. [Python Classes and Objects (Real Python)](https://realpython.com/python3-object-oriented-programming/)  

---

## 🚀 How to Run

Follow these steps to run the scripts:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/holbertonschool-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-classes
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

### 0. My first square
**File:** `0-square.py`  
Write an empty class `Square` that defines a square.

---

### 1. Square with size
**File:** `1-square.py`  
Add a private instance attribute `size` to the class `Square`.

---

### 2. Size validation
**File:** `2-square.py`  
Validate the `size` attribute:
- Raise a `TypeError` if `size` is not an integer.
- Raise a `ValueError` if `size` is less than 0.

---

### 3. Area of a square
**File:** `3-square.py`  
Add a method `area()` that calculates and returns the area of the square.

---

### 4. Access and update private attribute
**File:** `4-square.py`  
Add a getter and setter for the `size` attribute to:
- Retrieve the value of `size`.
- Validate and set a new value for `size`.

---

### 5. Printing a square
**File:** `5-square.py`  
Add a method `my_print()` that prints the square using the `#` character.

---

### 6. Coordinates of a square
**File:** `6-square.py`  
Add a private instance attribute `position` with:
- A getter and setter to validate and set the `position` attribute.
- Modify `my_print()` to use the `position` attribute for spacing.

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
```
