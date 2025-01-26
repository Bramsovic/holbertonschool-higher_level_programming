
# Python - Test-driven Development

## 📖 Description
This project focuses on **Test-Driven Development (TDD)**, a software development approach where tests are written **before** the actual code. By completing this project, you'll learn how to write proper documentation, create test cases to validate code functionality, and handle edge cases effectively. This approach ensures code reliability, maintainability, and correctness.

You will primarily use **doctest** and **unittest** modules in Python to write tests for functions and modules.

---

## 🎯 Learning Objectives
At the end of this project, you should be able to explain the following concepts **without external help**:

### General
- Why Python programming is awesome.
- What is an **interactive test**.
- Why **tests** are essential in software development.
- How to write **Docstrings** to create tests.
- How to write proper documentation for each module and function.
- What are the basic options/flags to create tests.
- How to identify and handle **edge cases** in your code.

---

## ✅ Requirements

### Python Scripts
- All files are interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.8.5**.
- The first line of all files must be:
  ```bash
  #!/usr/bin/python3
  ```
- All files must:
  - End with a **new line**.
  - Be **PEP 8 compliant** (verified with `pycodestyle` version 2.7.*).
  - Be **executable**.
  - Be tested for length using the `wc` command.

### Python Test Cases
- All test files must:
  - Be placed inside a `tests/` folder.
  - Use the `.txt` extension for **doctest** or `.py` for **unittest**.
  - Be executed using:
    ```bash
    python3 -m doctest ./tests/*
    ```
    or:
    ```bash
    python3 -m unittest discover tests
    ```
- Modules and functions must have proper documentation:
  - To test module documentation:
    ```bash
    python3 -c 'print(__import__("module_name").__doc__)'
    ```
  - To test function documentation:
    ```bash
    python3 -c 'print(__import__("module_name").function_name.__doc__)'
    ```

- Each test case should cover **all edge cases** for maximum reliability.

---

## 📚 Resources
To complete this project, refer to the following resources:

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) *(read until “26.2.3.7. Warnings” included)*.
- [doctest – Testing through documentation](https://realpython.com/python-testing/#doctest).
- [Unit Tests in Python](https://realpython.com/python-testing/#unittest).

---

## 🚀 How to Run Tests

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

### Examples:
- Run all doctests:
  ```bash
  python3 -m doctest -v ./tests/*
  ```
- Run a specific unittest file:
  ```bash
  python3 -m unittest tests/test_file_name.py
  ```

---

## 🛠️ Project Structure
This project contains the following files and folders:

```
python-test_driven_development/
├── 0-add_integer.py               # Adds two integers
├── 2-matrix_divided.py            # Divides all elements of a matrix
├── 3-say_my_name.py               # Prints a formatted name
├── 4-print_square.py              # Prints a square with #
├── 5-text_indentation.py          # Adds indentation to text
├── 6-max_integer.py               # Finds the max integer in a list
├── tests/                         # Folder containing test cases
│   ├── 0-add_integer.txt          # Doctest for 0-add_integer
│   ├── 2-matrix_divided.txt       # Doctest for 2-matrix_divided
│   ├── 3-say_my_name.txt          # Doctest for 3-say_my_name
│   ├── 4-print_square.txt         # Doctest for 4-print_square
│   ├── 5-text_indentation.txt     # Doctest for 5-text_indentation
│   ├── 6-max_integer_test.py      # Unittest for 6-max_integer
├── README.md                      # Project documentation
```

---

## 📝 Task Overview

### 0. Integers addition
**File:** `0-add_integer.py`  
Write a function `add_integer(a, b=98)` that adds two integers. Ensure proper input validation and raise exceptions for invalid inputs.  

- **Doctest file:** `tests/0-add_integer.txt`

---

### 1. Divide a matrix
**File:** `2-matrix_divided.py`  
Write a function `matrix_divided(matrix, div)` that divides all elements of a matrix by `div`. Validate inputs and handle edge cases.  

- **Doctest file:** `tests/2-matrix_divided.txt`

---

### 2. Say my name
**File:** `3-say_my_name.py`  
Write a function `say_my_name(first_name, last_name="")` that prints a properly formatted name. Ensure input validation for strings.  

- **Doctest file:** `tests/3-say_my_name.txt`

---

### 3. Print square
**File:** `4-print_square.py`  
Write a function `print_square(size)` that prints a square of `#` characters with the given size.  

- **Doctest file:** `tests/4-print_square.txt`

---

### 4. Text indentation
**File:** `5-text_indentation.py`  
Write a function `text_indentation(text)` that formats text by adding two new lines after `.`, `?`, and `:`. Ensure no spaces at the start or end of lines.  

- **Doctest file:** `tests/5-text_indentation.txt`

---

### 5. Max integer - Unittest
**File:** `6-max_integer.py`  
Write unittests for the function `max_integer(list=[])`. Test cases should handle empty lists, single elements, and various edge cases.  

- **Unittest file:** `tests/6-max_integer_test.py`

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
This project is licensed under the **MIT License**. You are free to use, modify, and distribute the code in compliance with the license terms.

---

Happy testing! 🧪✨