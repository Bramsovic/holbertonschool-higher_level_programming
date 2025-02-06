
# 🏗️ Python - Abstract Classes and Interfaces

Welcome to this project on **Abstract Classes, Interfaces, and Advanced OOP Concepts** in Python! 🐍  
This project explores **abstract base classes (ABCs)**, **duck typing**, **subclassing**, **mixins**, and **multiple inheritance**. You will gain hands-on experience in designing, implementing, and testing Python programs using OOP best practices.

---

## 📋 Table of Contents

1. [📖 Introduction](#-introduction)  
2. [🎯 Learning Objectives](#-learning-objectives)  
3. [✅ Requirements](#-requirements)  
4. [📂 Repository Structure](#-repository-structure)  
5. [📚 Resources](#-resources)  
6. [🚀 How to Run](#-how-to-run)  
7. [📝 Task Overview](#-task-overview)  
   - [0. Abstract Animal Class and its Subclasses](#0-abstract-animal-class-and-its-subclasses)  
   - [1. Shapes, Interfaces, and Duck Typing](#1-shapes-interfaces-and-duck-typing)  
   - [2. Extending the Python List with Notifications](#2-extending-the-python-list-with-notifications)  
   - [3. CountedIterator - Keeping Track of Iteration](#3-countediterator---keeping-track-of-iteration)  
   - [4. The Enigmatic FlyingFish - Exploring Multiple Inheritance](#4-the-enigmatic-flyingfish---exploring-multiple-inheritance)  
   - [5. The Mystical Dragon - Mastering Mixins](#5-the-mystical-dragon---mastering-mixins)  
8. [🤝 Contribution Guidelines](#-contribution-guidelines)  

---

## 📖 Introduction

This project focuses on **advanced Object-Oriented Programming (OOP)** concepts:  

- 🏛 **Abstract Classes & Interfaces**  
- 🦆 **Duck Typing & Polymorphism**  
- 🔗 **Subclassing & Overriding Methods**  
- 🎭 **Multiple Inheritance & Method Resolution Order (MRO)**  
- 🧩 **Mixins & Code Reusability**  

By the end of this project, you'll be proficient in **designing scalable, modular, and reusable OOP-based programs** in Python. 🐍🔥  

---

## 🎯 Learning Objectives

By completing this project, you will learn to:  

✔ **Use Abstract Classes** with the `abc` module.  
✔ **Implement Interfaces & Duck Typing** for flexible polymorphism.  
✔ **Extend Python’s built-in classes** to modify behaviors.  
✔ **Use Multiple Inheritance & MRO** for complex class hierarchies.  
✔ **Employ Mixins** to share behavior between unrelated classes.  

---

## ✅ Requirements

### **Python Scripts**
- **Python Version:** Python 3.8.5 (Ubuntu 20.04 LTS)  
- **Code Style:** PEP 8 compliant (`pycodestyle` version 2.7.*)  
- **Execution:**  
  - All files must start with:  
    ```python
    #!/usr/bin/python3
    ```
  - Must end with a **new line**  
  - Must be **executable** (`chmod +x script.py`)  

### **Documentation**
- **Docstrings** are **mandatory**:  
  - **Modules**, **Classes**, **Methods** must be documented using **Google Style Python Docstrings**.

---

## 📂 Repository Structure

```plaintext
python-abc/
├── task_00_abc.py            # Abstract Class for Animals (Dog, Cat)
├── task_01_duck_typing.py     # Abstract Shape Class (Circle, Rectangle) + Duck Typing
├── task_02_verboselist.py     # Extending Python List with Verbose Notifications
├── task_03_countediterator.py # Custom Iterator with Counter
├── task_04_flyingfish.py      # Multiple Inheritance (FlyingFish from Bird & Fish)
├── task_05_dragon.py          # Mixins (Dragon with FlyMixin & SwimMixin)
├── README.md                  # Project documentation
```

---

## 📚 Resources

### **Recommended Reading**
- 📖 [Python 3 Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)  
- 🔹 [ABC - Abstract Base Classes](https://docs.python.org/3/library/abc.html)  
- 🦆 [Duck Typing in Python](https://realpython.com/lessons/duck-typing/)  
- 🎥 [Corey Schafer - OOP Playlist (YouTube)](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)  

---

## 🚀 How to Run

1️⃣ Clone the repository:
   ```bash
   git clone https://github.com/your_username/holbertonschool-higher_level_programming.git
   ```

2️⃣ Navigate to the project directory:
   ```bash
   cd holbertonschool-higher_level_programming/python-abc
   ```

3️⃣ Make a script executable:
   ```bash
   chmod +x task_00_abc.py
   ```

4️⃣ Run the script:
   ```bash
   ./task_00_abc.py
   ```

---

## 📝 Task Overview

### 0️⃣ Abstract Animal Class and its Subclasses
📌 **File:** `task_00_abc.py`  
🏛 **Concepts:** Abstract Classes, Method Overriding  

✔ Create an **abstract class** `Animal` with an abstract method `sound()`.  
✔ Implement two subclasses:  
   - `Dog` → Returns `"Bark"`  
   - `Cat` → Returns `"Meow"`  

---

### 1️⃣ Shapes, Interfaces, and Duck Typing
📌 **File:** `task_01_duck_typing.py`  
🦆 **Concepts:** Interfaces, Duck Typing  

✔ Create an **abstract class** `Shape` with methods `area()` & `perimeter()`.  
✔ Implement two concrete classes:  
   - `Circle(radius)`  
   - `Rectangle(width, height)`  
✔ Define a **duck-typed function** `shape_info(shape)`.  

---

### 2️⃣ Extending the Python List with Notifications
📌 **File:** `task_02_verboselist.py`  
📜 **Concepts:** Inheritance, Overriding Built-in Methods  

✔ Create a subclass `VerboseList` extending Python’s `list`.  
✔ Override `append()`, `extend()`, `remove()`, and `pop()` to print messages.  

---

### 3️⃣ CountedIterator - Keeping Track of Iteration
📌 **File:** `task_03_countediterator.py`  
🔄 **Concepts:** Custom Iterators  

✔ Extend Python’s `iter()` to track the number of iterated items.  
✔ Implement a **custom iterator** `CountedIterator`.  

---

### 4️⃣ The Enigmatic FlyingFish - Exploring Multiple Inheritance
📌 **File:** `task_04_flyingfish.py`  
🦅🐟 **Concepts:** Multiple Inheritance, Method Resolution Order (MRO)  

✔ Create classes `Fish` & `Bird` with `swim()`, `fly()`, and `habitat()`.  
✔ Create `FlyingFish` inheriting from both.  

---

### 5️⃣ The Mystical Dragon - Mastering Mixins
📌 **File:** `task_05_dragon.py`  
🧩 **Concepts:** Mixins, Code Reusability  

✔ Implement mixins `SwimMixin` & `FlyMixin`.  
✔ Create a `Dragon` class inheriting from both mixins.  

---

## 🤝 Contribution Guidelines

🚀 **Want to contribute?**  

1️⃣ Fork the repository.  
2️⃣ Create a new branch:  
   ```bash
   git checkout -b feature-branch-name
   ```
3️⃣ Commit your changes:  
   ```bash
   git commit -m "Add a new feature"
   ```
4️⃣ Push to your branch:  
   ```bash
   git push origin feature-branch-name
   ```
5️⃣ Open a **Pull Request**!  

---

🔥 Happy Coding! 🚀🐍  
```
