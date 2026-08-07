# User Data Fetcher & JSON Parser

A Python-based utility designed to fetch user records from a public REST API (`JSONPlaceholder`), parse the response payload, output formatted details to the console, and persist the complete JSON data into a local file (`users.json`).

---

## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Prerequisites & Installation](#prerequisites--installation)
4. [Usage](#usage)
5. [GitHub Push Workflow](#github-push-workflow)

---

## Features
* **HTTP Requests:** Queries a public REST endpoint using `requests` with custom timeout handling.
* **Error Handling:** Leverages `raise_for_status()` and `try-except` blocks to handle connection or HTTP errors gracefully.
* **Data Parsing:** Parses JSON response arrays and extracts key fields (`name`, `email`, `city`) for console visualization[cite: 5].
* **File Persistence:** Automatically saves formatted JSON output to disk (`users.json`)[cite: 5].

---

## Project Structure

```text
.
├── public_api_data_fetcher.py # Python script for fetching, parsing, and storing data
├── users.json                 # Output JSON file where API data is stored
└── README.md                  # Project documentation



# Public API Data Fetcher & GitHub Workflow

A lightweight Python project that queries a public REST API (`JSONPlaceholder`), parses the response data, formats key user details to the console, saves the complete JSON output to disk (`users.json`), and documents the standard GitHub push workflow.

---

## Table of Contents
1. [Prerequisites & Installation](#prerequisites--installation)
2. [Usage](#usage)
3. [GitHub Push Workflow](#github-push-workflow)

---

## Prerequisites & Installation

### Requirements
* Python 3.x
* `requests` library

### Install Dependencies
Install the required HTTP library using `pip`:

```bash
pip install requests
