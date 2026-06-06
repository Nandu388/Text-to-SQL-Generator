# AI Text to SQL Generator

## Overview

AI Text to SQL Generator is a Flask-based Natural Language Processing (NLP) application that converts user text prompts into SQL queries automatically.

Users can enter natural language prompts such as:

* "Show top 5 employees"
* "Get product id and price"
* "Find customers older than 25"

and the system generates SQL queries dynamically.

The project works completely offline using NLP and spaCy without using Hugging Face or external AI APIs.

---

# Features

* Natural Language to SQL conversion
* Dynamic SQL query generation
* Offline working system
* NLP-based prompt understanding
* Modern responsive UI
* Supports multiple datasets
* Aggregate SQL functions
* WHERE conditions
* ORDER BY support
* LIMIT support
* Dynamic column detection

---

# Technologies Used

* Python
* Flask
* spaCy
* NLP
* HTML
* CSS
* Regex

---

# Project Structure

```plaintext
text_to_sql/
│
├── app.py
├── sql_generator.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# Installation

## Create Virtual Environment

```bash
python -m venv venv
```

---

# Activate Virtual Environment

## Windows PowerShell

```powershell
.\venv\Scripts\activate
```

---

# Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

# Run Project

```bash
python app.py
```

---

# Open Browser

```plaintext
http://127.0.0.1:5000
```

---

# Supported SQL Operations

* SELECT
* WHERE
* LIMIT
* ORDER BY
* COUNT
* AVG
* MAX
* MIN

---

# Example Inputs and Outputs

## Input

```plaintext
Get product id and price
```

## Output

```sql
SELECT id, price FROM products;
```

---

## Input

```plaintext
Find customers older than 25
```

## Output

```sql
SELECT * FROM customers WHERE age > 25;
```
<img width="1920" height="1020" alt="Screenshot 2026-06-06 211137" src="https://github.com/user-attachments/assets/ffc7fa66-28cd-41e3-bfa7-675d168af736" />


# Future Enhancements

* MySQL integration
* PostgreSQL support
* SQLite execution
* SQL validation
* Query history
* Voice to SQL
* AI-based query optimization
* Export queries
* Authentication system

---

# Advantages

* Easy to use
* Beginner friendly
* Offline working
* Fast query generation
* Modern user interface
* No API required

---

# Author

Developed using Flask and NLP for intelligent Text to SQL query generation.
