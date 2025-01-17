# Python - If/Else, Loops, and Functions

## 📖 Description
This project introduces Python concepts focusing on **if/else statements**, **loops**, and **functions**. It covers essential programming topics such as flow control, iteration, function definitions, and working with variables. The tasks are designed to help you practice and master Python basics, making you comfortable with these core concepts.

---

## 🎯 Learning Objectives
By the end of this project, you should be able to explain the following concepts **without external assistance**:

### General
- Why **indentation** is important in Python.
- How to use **if**, **if...else** statements.
- The purpose of **comments** in code and how to write them effectively.
- How to assign values to **variables**.
- How to use the **while** and **for** loops for iteration.
- The use of **break** and **continue** statements to control loop execution.
- How to use **else clauses** in loops.
- What the **pass** statement does and when to use it.
- How to use the **range** function.
- What a **function** is and how to define and use one.
- What happens when a function does not include a `return` statement.
- Understanding **variable scopes**: local and global.
- How to interpret a Python **traceback**.
- What **arithmetic operators** are and how to use them.

---

## ✅ Requirements

### Python Scripts
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.8.\***.
- The first line of every file must be:
  ```bash
  #!/usr/bin/python3
  ```
- All files must:
  - End with a **new line**.
  - Be **executable**.
  - Follow the **PEP 8** coding style (verified using `pycodestyle` version 2.7.\*).
  - Be tested for length using the `wc` command.
  
### Allowed Editors
- `vi`, `vim`, or `emacs`.

---

## 📚 Resources
To successfully complete this project, you may find the following resources helpful:

- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) *(Read until “4.6. Defining Functions” included)*.
- [IndentationError Explanation](https://docs.python.org/3/reference/lexical_analysis.html#indentation).
- [How To Use String Formatters in Python 3](https://realpython.com/python-string-formatting/).
- [Learn to Program 2: Looping (YouTube Playlist)](https://www.youtube.com/playlist?list=PL1B24DF1B61636B24).
- [Pycodestyle: Python Style Guide](https://pycodestyle.readthedocs.io/).

For built-in help:
- Use `man python3` for Python documentation.
- Use Python's `help()` function in the interpreter.

---

## 🚀 Tasks

### 0. Positive anything is better than negative nothing
**File:** `0-positive_or_negative.py`  
Write a program that assigns a random signed number to the variable `number` and prints whether the number is positive, negative, or zero.  

#### Example Output:
```bash
$ ./0-positive_or_negative.py
-4 is negative
$ ./0-positive_or_negative.py
0 is zero
$ ./0-positive_or_negative.py
6 is positive
```

---

### 1. The last digit
**File:** `1-last_digit.py`  
Write a program that assigns a random signed number to the variable `number` and prints its last digit, along with additional conditions based on its value.  

#### Example Output:
```bash
$ ./1-last_digit.py
Last digit of 626 is 6 and is greater than 5
$ ./1-last_digit.py
Last digit of -15 is -5 and is less than 6 and not 0
```

---

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
**File:** `2-print_alphabet.py`  
Write a program that prints the ASCII alphabet in lowercase, followed by no new line.  

#### Example Output:
```bash
$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyz
```

---

### 3. When I was having that alphabet soup, I never thought that it would pay off
**File:** `3-print_alphabt.py`  
Write a program that prints the ASCII alphabet in lowercase, excluding the letters `q` and `e`, followed by no new line.  

#### Example Output:
```bash
$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyz
```

---

### 4. Hexadecimal printing
**File:** `4-print_hexa.py`  
Write a program that prints all numbers from 0 to 98 in both decimal and hexadecimal formats.

#### Example Output:
```bash
$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
...
98 = 0x62
```

---

### 5. 00...99
**File:** `5-print_comb2.py`  
Write a program that prints numbers from 0 to 99, separated by `, `, with each number formatted to have two digits.  

#### Example Output:
```bash
$ ./5-print_comb2.py
00, 01, 02, ..., 98, 99
```

---

### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
**File:** `6-print_comb3.py`  
Write a program that prints all possible combinations of two digits, ensuring the smallest combination is printed first.  

#### Example Output:
```bash
$ ./6-print_comb3.py
01, 02, 03, ..., 89
```

---

### 7. islower
**File:** `7-islower.py`  
Write a function `islower(c)` that checks if a character is lowercase.

#### Example Output:
```python
>>> islower("a")
True
>>> islower("H")
False
```

---

### 8. To uppercase
**File:** `8-uppercase.py`  
Write a function `uppercase(str)` that prints a string in uppercase.

#### Example Output:
```python
>>> uppercase("best")
BEST
>>> uppercase("Holberton School")
HOLBERTON SCHOOL
```

---

### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
**File:** `9-print_last_digit.py`  
Write a function `print_last_digit(number)` that prints the last digit of a number.

#### Example Output:
```python
>>> print_last_digit(1234)
4
>>> print_last_digit(-42)
2
```

---

### 10. a + b
**File:** `10-add.py`  
Write a function `add(a, b)` that adds two integers and returns the result.

---

### 11. a ^ b
**File:** `11-pow.py`  
Write a function `pow(a, b)` that computes `a` raised to the power of `b`.

---

### 12. Fizz Buzz
**File:** `12-fizzbuzz.py`  
Write a function `fizzbuzz()` that prints numbers from 1 to 100. For multiples of 3, print `Fizz`. For multiples of 5, print `Buzz`. For multiples of both, print `FizzBuzz`.

---

## 🤝 Contribution Guidelines
Contributions are welcome! If you'd like to contribute:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature or fix"
   ```
4. Push the changes:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a Pull Request.

---

## 👨‍💻 Author
This project is part of the **Holberton School Higher-Level Programming** curriculum.

---

## 🛡️ License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code in compliance with the license terms.
```