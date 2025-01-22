
# 📘 Python - More Data Structures: Set, Dictionary

This repository contains solutions to tasks related to **advanced Python data structures**, specifically sets and dictionaries. These tasks are part of the **Holberton School** curriculum and are designed to improve our understanding of Python's capabilities in managing data efficiently.

---

## 📋 Table of Contents

1. [📖 Description](#-description)  
2. [🎯 Learning Objectives](#-learning-objectives)  
3. [⚙️ Requirements](#%EF%B8%8F-requirements)  
4. [🚀 Tasks](#-tasks)  
   - [0. Squared simple](#0-squared-simple)  
   - [1. Search and replace](#1-search-and-replace)  
   - [2. Unique addition](#2-unique-addition)  
   - [3. Present in both](#3-present-in-both)  
   - [4. Only differents](#4-only-differents)  
   - [5. Number of keys](#5-number-of-keys)  
   - [6. Print sorted dictionary](#6-print-sorted-dictionary)  
   - [7. Update dictionary](#7-update-dictionary)  
   - [8. Simple delete by key](#8-simple-delete-by-key)  
   - [9. Multiply by 2](#9-multiply-by-2)  
   - [10. Best score](#10-best-score)  
   - [11. Multiply by using map](#11-multiply-by-using-map)  
   - [12. Roman to Integer](#12-roman-to-integer)  
5. [📂 Repository Structure](#-repository-structure)  
6. [📊 Examples](#-examples)  

---

## 📖 Description

In this project, we explore Python's **sets** and **dictionaries**, which are powerful tools for handling data efficiently. Additionally, we learn about **lambda functions**, and Python's functional programming tools like `map`, `filter`, and `reduce`.

### Key Topics:
- Advanced use of **sets** for unique data management.
- Efficient data handling with **dictionaries**.
- Functional programming with **lambda**, `map`, `filter`, and `reduce`.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:
1. Understand and apply **sets** and their methods.
2. Know when to use **sets** vs **lists**.
3. Iterate through **sets** and **dictionaries**.
4. Efficiently use **dictionaries** for key-value mapping.
5. Differentiate between **dictionaries**, **lists**, and **sets**.
6. Write and apply **lambda functions**.
7. Use Python's **map**, **filter**, and **reduce** functions effectively.

---

## ⚙️ Requirements

- **Python Version:** Python 3.8.5 on Ubuntu 20.04 LTS.  
- **Code Style:** Follows `pycodestyle` (version 2.7.*).  
- **Mandatory Files:** A `README.md` file is required.  
- **Execution:** All scripts must be executable and start with `#!/usr/bin/python3`.  

---

## 🚀 Tasks

### 0. Squared simple
Write a function that computes the square of all integers in a matrix.
- **Prototype:** `def square_matrix_simple(matrix=[])`

### 1. Search and replace
Write a function that replaces all occurrences of an element by another in a new list.
- **Prototype:** `def search_replace(my_list, search, replace)`

### 2. Unique addition
Write a function that adds all unique integers in a list.
- **Prototype:** `def uniq_add(my_list=[])`

### 3. Present in both
Write a function that returns a set of common elements in two sets.
- **Prototype:** `def common_elements(set_1, set_2)`

### 4. Only differents
Write a function that returns a set of elements present in only one of two sets.
- **Prototype:** `def only_diff_elements(set_1, set_2)`

### 5. Number of keys
Write a function that returns the number of keys in a dictionary.
- **Prototype:** `def number_keys(a_dictionary)`

### 6. Print sorted dictionary
Write a function that prints a dictionary with keys sorted in alphabetical order.
- **Prototype:** `def print_sorted_dictionary(a_dictionary)`

### 7. Update dictionary
Write a function that replaces or adds a key-value pair in a dictionary.
- **Prototype:** `def update_dictionary(a_dictionary, key, value)`

### 8. Simple delete by key
Write a function that deletes a key in a dictionary.
- **Prototype:** `def simple_delete(a_dictionary, key="")`

### 9. Multiply by 2
Write a function that returns a new dictionary with all values multiplied by 2.
- **Prototype:** `def multiply_by_2(a_dictionary)`

### 10. Best score
Write a function that returns the key with the highest value in a dictionary.
- **Prototype:** `def best_score(a_dictionary)`

### 11. Multiply by using map
Write a function that returns a list of values multiplied by a number using `map`.
- **Prototype:** `def multiply_list_map(my_list=[], number=0)`

### 12. Roman to Integer
Write a function that converts a Roman numeral to an integer.
- **Prototype:** `def roman_to_int(roman_string)`

---

## 📂 Repository Structure

```plaintext
.
├── README.md                   # Project documentation
├── 0-square_matrix_simple.py   # Task 0 solution
├── 1-search_replace.py         # Task 1 solution
├── 2-uniq_add.py               # Task 2 solution
├── 3-common_elements.py        # Task 3 solution
├── 4-only_diff_elements.py     # Task 4 solution
├── 5-number_keys.py            # Task 5 solution
├── 6-print_sorted_dictionary.py# Task 6 solution
├── 7-update_dictionary.py      # Task 7 solution
├── 8-simple_delete.py          # Task 8 solution
├── 9-multiply_by_2.py          # Task 9 solution
├── 10-best_score.py            # Task 10 solution
├── 11-multiply_list_map.py     # Task 11 solution
└── 12-roman_to_int.py          # Task 12 solution
```

---

## 📊 Examples

### Task 0: Squared simple
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_matrix = square_matrix_simple(matrix)
print(new_matrix)  # Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```

### Task 1: Search and replace
```python
my_list = [1, 2, 3, 2, 1]
new_list = search_replace(my_list, 2, 42)
print(new_list)  # Output: [1, 42, 3, 42, 1]
```

---

Thank you for exploring the **Python - More Data Structures: Set, Dictionary** project! If you have any feedback or suggestions, feel free to share them. 😊
