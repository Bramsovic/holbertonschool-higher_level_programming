
# Python Import Modules

## 📖 Description
This project is designed to help you understand and master the use of **modules**, **imports**, and **command-line arguments** in Python. By completing these tasks, you will learn how to create modular Python programs, leverage reusable code, and handle external inputs efficiently.

---

## 🎯 Learning Objectives
At the end of this project, you should be able to:

### General
- Explain why Python programming is awesome.
- Import functions from another file.
- Use imported functions effectively.
- Create and use Python **modules**.
- Utilize the built-in **`dir()`** function to inspect objects and modules.
- Prevent code in your script from being executed when it is imported.
- Handle **command-line arguments** in Python programs.

---

## ✅ Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`.
- All Python scripts will be interpreted/compiled on **Ubuntu 22.04 LTS** using **Python 3.10.\***.
- All files must:
  - End with a **new line**.
  - Include a shebang on the first line:
    ```bash
    #!/usr/bin/python3
    ```
  - Be **PEP 8 compliant**, verified using **`pycodestyle` version 2.7.\***.
  - Be **executable**.
  - Have lengths verified using the `wc` command.
- A `README.md` file at the root of the project folder is mandatory.

---

## 📚 Resources
To complete this project, you may find the following resources helpful:

- [Modules in Python](https://docs.python.org/3/tutorial/modules.html)
- [Command Line Arguments in Python](https://docs.python.org/3/library/argparse.html)
- [Pycodestyle – Style Guide for Python Code](https://pycodestyle.readthedocs.io/)

For additional help, you can also use the built-in tools:
- `man python3`
- Python's interactive `help()` function.

---

## 🚀 Tasks

### 0. Import a simple function from a simple file
**File:** `0-add.py`  
Write a program that imports the function `add(a, b)` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.  

#### Requirements:
- Use the `print` function with string formatting to display integers.
- Assign:
  - `1` to a variable `a`.
  - `2` to a variable `b`.
- Use the variables as arguments when calling the functions `add` and `print`.
- The script should print:
  ```
  <a value> + <b value> = <add(a, b) value>
  ```
- The `add_0` module should only be imported once in your code.
- Avoid using `*` for importing or `__import__`.

#### Example:
```bash
$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """Adds two integers."""
    return a + b

$ ./0-add.py
1 + 2 = 3
```

---

### 1. My first toolbox!
**File:** `1-calculation.py`  
Write a program that imports functions from the file `calculator_1.py`, performs arithmetic operations, and prints the results.

#### Requirements:
- Assign:
  - `10` to a variable `a`.
  - `5` to a variable `b`.
- Call each imported function (`add`, `sub`, `mul`, `div`) and print their results.
- Use string formatting for output.
- Ensure the module `calculator_1` is imported only once.

#### Example:
```bash
$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a // b

$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

---

### 2. How to make a script dynamic!
**File:** `2-args.py`  
Write a program that prints the number of and the list of its arguments.

#### Requirements:
- The output should include:
  - The number of arguments.
  - The list of arguments (one per line) with their position and value.
- Handle cases where no arguments are passed.

#### Example:
```bash
$ ./2-args.py 
0 arguments.

$ ./2-args.py Hello
1 argument:
1: Hello

$ ./2-args.py Hello Welcome To Python
4 arguments:
1: Hello
2: Welcome
3: To
4: Python
```

---

### 3. Infinite addition
**File:** `3-infinite_add.py`  
Write a program that calculates and prints the sum of all its command-line arguments.

#### Requirements:
- Convert arguments to integers using `int()`.
- Print the result of the addition, followed by a new line.

#### Example:
```bash
$ ./3-infinite_add.py 
0

$ ./3-infinite_add.py 10 20 30
60
```

---

### 4. Who are you?
**File:** `4-hidden_discovery.py`  
Write a program that prints all names defined by the compiled module `hidden_4.pyc`.

#### Requirements:
- Print one name per line in alphabetical order.
- Exclude names starting with `__`.

#### Example:
```bash
$ ./4-hidden_discovery.py
my_secret
print_hidden
```

---

### 5. Everything can be imported
**File:** `5-variable_load.py`  
Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

#### Requirements:
- Do not use `*` for importing or `__import__`.

#### Example:
```bash
$ cat variable_load_5.py
#!/usr/bin/python3
a = 98

$ ./5-variable_load.py
98
```

---

## 🤝 Contribution Guidelines
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push your changes:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request and describe your changes.

---

## 👨‍💻 Author
This project is part of the Holberton School Higher-Level Programming curriculum.

---

## 🛡️ License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it under the terms of the license.
```