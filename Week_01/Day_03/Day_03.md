# Day 3: Python Practice — OOP, APIs & File I/O

A foundational guide covering key Python concepts for software development and cybersecurity automation, including Object-Oriented Programming (OOP), network HTTP requests, JSON serialization, safe file operations, and REST API consumption.

---

## Table of Contents
1. [Object-Oriented Programming (OOP)](#1-object-oriented-programming-oop)
2. [HTTP Requests with `requests`](#2-http-requests-with-requests)
3. [JSON Data Handling (`json` Module)](#3-json-data-handling-json-module)
4. [File Handling & Context Managers](#4-file-handling--context-managers)
5. [REST APIs & HTTP Methods](#5-rest-apis--http-methods)

---

## 1. Object-Oriented Programming (OOP)

OOP organizes code into reusable blueprints called **Classes** to create **Objects** (instances).

### Key Concepts
* **Class:** The blueprint defining attributes (data) and methods (behavior).
* **`__init__`:** The constructor method that initializes an object's attributes upon creation.
* **`self`:** Represents the specific instance of the class accessing methods or data.
* **Encapsulation:** Hiding internal data and restricting direct access using private attributes (prefixed with double underscores `__`).

---

## 2. HTTP Requests with `requests`

In Python, `requests` is a highly popular, third-party library used to send HTTP requests to interact with web servers and APIs. It simplifies network communication by abstracting complex configurations into a human-friendly syntax, making tasks like data scraping or API integration effortless.

### Installation
```bash
pip install requests
```

---

## 3. JSON Data Handling (`json` Module)

Python handles JSON data using its built-in `json` module, which provides functions to convert Python objects to JSON strings (and vice versa) and to read or write JSON files.

### The 4 Core Functions
> **Memory Trick:** Functions ending in **"s"** interact with **S**trings; functions **without** an "s" interact with **Files**.

| Function | Action | Input $
ightarrow$ Output |
| :--- | :--- | :--- |
| `json.loads()` | **Load S**tring | JSON String $
ightarrow$ Python Dictionary/List |
| `json.dumps()` | **Dump S**tring | Python Dictionary/List $
ightarrow$ JSON String |
| `json.load()` | **Load** File | JSON File Object $
ightarrow$ Python Dictionary/List |
| `json.dump()` | **Dump** File | Python Dictionary/List $
ightarrow$ JSON File Object |

---

## 4. File Handling & Context Managers

File handling in Python is managed using the built-in `open()` function, which creates a file object to read, write, modify, or delete files. 

The most secure and efficient way to handle files is by using the `with` statement context manager, which automatically closes the file after its code block finishes, preventing memory leaks and data corruption.

### Common File Access Modes
* `'r'` — Read mode (default)
* `'w'` — Write mode (creates a new file or overwrites an existing file)
* `'a'` — Append mode (adds data to the end of an existing file)

---

## 5. REST APIs & HTTP Methods

Python is one of the most popular languages for building and consuming REST APIs due to its clean syntax and powerful ecosystem of frameworks. A REST API allows different software applications to communicate over HTTP using standard methods:

### Standard Methods Overview

| Method | CRUD Equivalent | Description |
| :--- | :--- | :--- |
| **GET** | Read | Retrieves data from a server. |
| **POST** | Create | Sends new data to a server. |
| **PUT** | Update | Replaces or updates existing data on a server. |
| **DELETE** | Delete | Removes data from a server. |
