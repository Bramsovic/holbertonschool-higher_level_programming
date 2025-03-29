# Python - Serialization

## Novice Level Project

**GitHub Repo:** `holbertonschool-higher_level_programming`  
**Directory:** `python-serialization`  
**Weight:** 1  

---

## 🧠 Description

Welcome to an introduction to **Marshaling** and **Serialization**—key concepts in managing, storing, and transmitting data efficiently. This project covers:

- Object-Oriented Programming with marshaling and serialization in Python
- Binary data handling with the `pickle` module
- Data conversion between CSV, JSON, and XML formats

These skills are vital for tasks such as data persistence, inter-system communication, and web/database interactions.

---

## 🧾 Learning Objectives

- Understand marshaling vs. serialization
- Perform data serialization and deserialization in Python
- Use serialization in networking, web, and database contexts
- Compare performance across JSON, XML, and binary formats

---

## 📚 Resources

- [Real Python: Serialization](https://realpython.com/python-serialization/)
- [Working With JSON Data](https://realpython.com/python-json/)
- [Python `pickle` Docs](https://docs.python.org/3/library/pickle.html)
- [Corey Schafer on Pickle](https://www.youtube.com/watch?v=2Tw39kZIbhs)
- [CSV to JSON in Python](https://realpython.com/python-csv/)
- [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Socket Programming Guide](https://realpython.com/python-sockets/)

---

## ✅ Tasks Overview

### 0. Basic Serialization (✔️ Completed)

**File:** `task_00_basic_serialization.py`  
Serialize a Python dictionary to a JSON file and deserialize it back.

```python
def serialize_and_save_to_file(data, filename):
    ...

def load_and_deserialize(filename):
    ...
```

**Example:**

```python
data_to_serialize = {"name": "John Doe", "age": 30, "city": "New York"}
serialize_and_save_to_file(data_to_serialize, 'data.json')
deserialized_data = load_and_deserialize('data.json')
```

---

### 1. Pickling Custom Classes (✔️ Mostly Completed)

**File:** `task_01_pickle.py`  
Create a `CustomObject` class with `name`, `age`, `is_student`, and methods to pickle and unpickle instances.

```python
class CustomObject:
    def serialize(self, filename): ...
    @classmethod
    def deserialize(cls, filename): ...
    def display(self): ...
```

Handles exceptions gracefully by returning `None` for errors.

---

### 2. Converting CSV Data to JSON Format (✔️ Completed)

**File:** `task_02_csv.py`  
Read from CSV and convert data into JSON format using `csv.DictReader`.

```python
def convert_csv_to_json(csv_filename): ...
```

Handles missing files and returns `False` on failure.

---

### 3. Serializing and Deserializing with XML (✔️ Mostly Completed)

**File:** `task_03_xml.py`  
Use `xml.etree.ElementTree` to convert dictionaries to and from XML.

```python
def serialize_to_xml(dictionary, filename): ...
def deserialize_from_xml(filename): ...
```

Note: Type conversions are required since XML treats all data as strings.

---

## 📂 File Structure

```
python-serialization/
│
├── task_00_basic_serialization.py
├── task_01_pickle.py
├── task_02_csv.py
├── task_03_xml.py
└── README.md
```

---

## 📈 Progress

- [x] Task 0: Basic Serialization
- [x] Task 1: Pickling Custom Classes (75%)
- [x] Task 2: CSV to JSON
- [x] Task 3: XML Serialization (65%)




---

## 📬 License

This project is for educational purposes under Holberton School curriculum guidelines.
