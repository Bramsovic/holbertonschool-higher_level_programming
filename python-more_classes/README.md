

# 🏗️ Python - More Classes and Objects

This project is part of the **Holberton School Higher-Level Programming** curriculum. It expands on **Object-Oriented Programming (OOP)** principles in Python, focusing on class attributes, special methods (`__str__`, `__repr__`), static and class methods, and memory management using destructors.

---

## 📋 Table of Contents

1. [📖 Background Context](#-background-context)  
2. [🎯 Learning Objectives](#-learning-objectives)  
3. [✅ Requirements](#-requirements)  
4. [📂 Repository Structure](#-repository-structure)  
5. [📚 Resources](#-resources)  
6. [🚀 How to Run](#-how-to-run)  
7. [📝 Task Overview](#-task-overview)  
   - [0. Simple rectangle](#0-simple-rectangle)  
   - [1. Real definition of a rectangle](#1-real-definition-of-a-rectangle)  
   - [2. Area and Perimeter](#2-area-and-perimeter)  
   - [3. String representation](#3-string-representation)  
   - [4. Eval is magic](#4-eval-is-magic)  
   - [5. Detect instance deletion](#5-detect-instance-deletion)  
   - [6. How many instances](#6-how-many-instances)  
   - [7. Change representation](#7-change-representation)  
   - [8. Compare rectangles](#8-compare-rectangles)  
   - [9. A square is a rectangle](#9-a-square-is-a-rectangle)  
8. [🤝 Contribution Guidelines](#-contribution-guidelines)  
9. [👨‍💻 Author](#-author)  

---

## 📖 Background Context

This project builds upon the foundation of **Object-Oriented Programming (OOP)** in Python. The goal is to explore **class attributes, special methods, and memory management** to develop more complex classes and objects.

It is important to **experiment** with the provided concepts, modify examples, and test edge cases. **Play with OOP concepts** to better understand how they function in real-world applications.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

### **OOP Fundamentals**
- Understand **Object-Oriented Programming (OOP)** principles.
- Define **classes, objects, and instances** in Python.
- Differentiate between **class attributes** and **instance attributes**.
- Work with **public, protected, and private attributes**.
- Understand **Data Abstraction, Encapsulation, and Information Hiding**.

### **Advanced Class Features**
- Implement **properties, getters, and setters** the Pythonic way.
- Utilize **special methods** such as `__str__` and `__repr__`.
- Understand the difference between **`str()` and `repr()`**.
- Create and use **static methods** and **class methods**.
- Manage **class attributes** and modify them dynamically.
- Implement **destructors (`__del__`)** for memory management.

---

## ✅ Requirements

### **Python Scripts**
- **Python Version:** All files are interpreted/compiled using **Python 3.8.5** on **Ubuntu 20.04 LTS**.
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

### **Documentation**
- **Docstrings** are **mandatory** for:
  - **Modules**: Each module must have a docstring describing its purpose.
  - **Classes**: Each class must have a docstring describing its role.
  - **Methods/Functions**: Each function or method (inside or outside a class) must have a docstring explaining its purpose and behavior.
  - Use **Google Style Python Docstrings** for documentation.

### **Allowed Editors**
- `vi`, `vim`, or `emacs`.

---

## 📂 Repository Structure

```plaintext
python-more_classes/
├── 0-rectangle.py      # Defines an empty Rectangle class
├── 1-rectangle.py      # Adds width and height with validation
├── 2-rectangle.py      # Adds methods for area and perimeter calculation
├── 3-rectangle.py      # Adds string representation of the rectangle
├── 4-rectangle.py      # Adds __repr__ method to allow object recreation
├── 5-rectangle.py      # Adds destructor (__del__) to detect deletion
├── 6-rectangle.py      # Adds a class attribute to count instances
├── 7-rectangle.py      # Adds a class attribute to change print symbol
├── 8-rectangle.py      # Adds a static method to compare rectangles
├── 9-rectangle.py      # Adds a class method to create a square
├── README.md           # Project documentation
```

---

## 📚 Resources

To complete this project, refer to the following resources **in order**:

1. [Object Oriented Programming (Python.org)](https://docs.python.org/3/tutorial/classes.html) (Read everything until "Inheritance" **excluded**)
2. [Class and Instance Attributes](https://realpython.com/python3-object-oriented-programming/#class-and-instance-attributes)
3. [str vs repr](https://realpython.com/python-str-vs-repr/)
4. [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)  

---

## 🚀 How to Run

Follow these steps to run the scripts:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/holbertonschool-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-more_classes
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

### 0. Simple rectangle
**File:** `0-rectangle.py`  
Write an empty class `Rectangle`.

---

### 1. Real definition of a rectangle
**File:** `1-rectangle.py`  
Add attributes `width` and `height` with validation.

---

### 2. Area and Perimeter
**File:** `2-rectangle.py`  
Add methods to calculate **area** and **perimeter**.

---

### 3. String representation
**File:** `3-rectangle.py`  
Define `__str__` to return a string representation of the rectangle.

---

### 4. Eval is magic
**File:** `4-rectangle.py`  
Define `__repr__` to return a string for recreating the instance.

---

### 5. Detect instance deletion
**File:** `5-rectangle.py`  
Add `__del__` to print a message when an instance is deleted.

---

### 6. How many instances
**File:** `6-rectangle.py`  
Add a class attribute to count instances of `Rectangle`.

---

### 7. Change representation
**File:** `7-rectangle.py`  
Modify `print_symbol` to allow custom symbols for string representation.

---

### 8. Compare rectangles
**File:** `8-rectangle.py`  
Implement a **static method** to compare rectangle areas.

---

### 9. A square is a rectangle
**File:** `9-rectangle.py`  
Implement a **class method** to create a square (`width == height`).

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
