# Python - Inheritance

## 📖 Description
This project covers the **concept of inheritance in Python**, a fundamental principle of **Object-Oriented Programming (OOP)**.  
By completing these exercises, you will understand how to create classes, inherit attributes and methods from parent classes, and work with built-in Python functions for inheritance-related operations.

---

## 🎯 Learning Objectives
By the end of this project, you should be able to explain the following concepts **without external help**:

### General
- What is a **superclass**, **base class**, or **parent class**.
- What is a **subclass**.
- How to **list all attributes and methods** of a class or instance.
- When an **instance** can have new attributes.
- How to **inherit** a class from another.
- How to **define a class with multiple base classes**.
- What is the **default class** every class inherits from.
- How to **override methods or attributes** inherited from a base class.
- Which **attributes and methods are inherited** by subclasses.
- The **purpose of inheritance**.
- How and when to use:
  - `isinstance()`
  - `issubclass()`
  - `type()`
  - `super()`

---

## ✅ Requirements

### Python Scripts
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.8.5**.
- The first line of every file must be:
  ```bash
  #!/usr/bin/python3
  ```
- All files must:
  - End with a **new line**.
  - Follow the **PEP 8** coding style (`pycodestyle` version 2.7.*).
  - Be **executable**.
  - Be tested for length using the `wc` command.

### Python Test Cases
- All test files must be inside the `tests/` directory.
- Test files should:
  - Have a `.txt` extension for **doctest** or `.py` for **unittest**.
  - Be executed using:
    ```bash
    python3 -m doctest ./tests/*
    ```
    or:
    ```bash
    python3 -m unittest discover tests
    ```
- Documentation rules:
  - **Modules** must have a docstring:
    ```bash
    python3 -c 'print(__import__("my_module").__doc__)'
    ```
  - **Classes** must have a docstring:
    ```bash
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    ```
  - **Functions** inside and outside classes must have a docstring:
    ```bash
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    ```
- **All edge cases** must be covered in your tests.

---

## 📚 Resources
To complete this project, review the following:

- [Python Documentation: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://realpython.com/inheritance-composition-python/)
- [Learn to Program 10: Inheritance Magic Methods](https://www.youtube.com/watch?v=RSl87lqOXDE)

---

## 🚀 How to Run

### Running Doctests
1. Navigate to the `tests/` folder:
   ```bash
   cd tests
   ```
2. Run the doctests using:
   ```bash
   python3 -m doctest -v ./<test_file>.txt
   ```

### Running Unittests
1. Navigate to the project directory.
2. Run all unittests in the `tests/` folder:
   ```bash
   python3 -m unittest discover tests
   ```

### Example:
- Run all doctests:
  ```bash
  python3 -m doctest -v ./tests/*
  ```
- Run a specific unittest file:
  ```bash
  python3 -m unittest tests/test_file_name.py
  ```

---

## 📂 Project Structure
This project is structured as follows:

```
python-inheritance/
├── 0-lookup.py                # Returns attributes and methods of an object
├── 1-my_list.py               # Inherits from list and sorts items
├── 2-is_same_class.py         # Checks if an object is exactly an instance of a class
├── 3-is_kind_of_class.py      # Checks if an object is an instance of a class or its subclass
├── 4-inherits_from.py         # Checks if an object is a subclass
├── 5-base_geometry.py         # Empty BaseGeometry class
├── 6-base_geometry.py         # BaseGeometry with area() method
├── 7-base_geometry.py         # BaseGeometry with integer validation
├── 8-rectangle.py             # Rectangle class inheriting from BaseGeometry
├── 9-rectangle.py             # Rectangle class with implemented __str__
├── 10-square.py               # Square class inheriting from Rectangle
├── 11-square.py               # Square class with implemented __str__
├── tests/                     # Folder for test cases
│   ├── 1-my_list.txt          # Doctest for 1-my_list
│   ├── 7-base_geometry.txt    # Doctest for 7-base_geometry
│   ├── test_inheritance.py    # Unittests for various inheritance functions
├── README.md                  # Project documentation
```

---

## 📝 Task Overview

### 0. Lookup
**File:** `0-lookup.py`  
Write a function `lookup(obj)` that returns the list of available attributes and methods of an object.

---

### 1. My list
**File:** `1-my_list.py`  
Write a class `MyList` that inherits from `list`.  
- Includes `print_sorted(self)`, which prints the list in ascending order.

---

### 2. Exact same object
**File:** `2-is_same_class.py`  
Write a function `is_same_class(obj, a_class)` that returns `True` if `obj` is exactly an instance of `a_class`, otherwise `False`.

---

### 3. Same class or inherit from
**File:** `3-is_kind_of_class.py`  
Write a function `is_kind_of_class(obj, a_class)` that returns `True` if `obj` is an instance of `a_class` or an instance of a class that inherited from `a_class`.

---

### 4. Only sub class of
**File:** `4-inherits_from.py`  
Write a function `inherits_from(obj, a_class)` that returns `True` if `obj` is an instance of a class that **inherited (directly or indirectly)** from `a_class`.

---

### 5. Geometry module
**File:** `5-base_geometry.py`  
Write an empty class `BaseGeometry`.

---

### 6. Improve Geometry
**File:** `6-base_geometry.py`  
Update `BaseGeometry` with `area(self)`, which raises an Exception `"area() is not implemented"`.

---

### 7. Integer validator
**File:** `7-base_geometry.py`  
Update `BaseGeometry` with `integer_validator(self, name, value)`, which validates integers.

---

### 8. Rectangle
**File:** `8-rectangle.py`  
Create a class `Rectangle` that inherits from `BaseGeometry`.

---

### 9. Full rectangle
**File:** `9-rectangle.py`  
Update `Rectangle` to implement the `__str__` method.

---

### 10. Square #1
**File:** `10-square.py`  
Create a class `Square` that inherits from `Rectangle`.

---

### 11. Square #2
**File:** `11-square.py`  
Update `Square` to implement the `__str__` method.

---

## 🤝 Contribution Guidelines

Contributions are welcome! To contribute:

1. **Fork** this repository.
2. Create a **feature branch**:
   ```bash
   git checkout -b feature-branch-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Add a feature or fix a bug"
   ```
4. **Push your branch**:
   ```bash
   git push origin feature-branch-name
   ```
5. **Submit a Pull Request**.

---

## 👨‍💻 Author
This project is part of the **Holberton School Higher-Level Programming** curriculum.

---

## 🛡️ License
This project is licensed under the **MIT License**.