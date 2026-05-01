# ☕ SmartCafe - Cafe Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

A clean, console-based cafe management system built with Python to streamline order processing, menu management, and revenue tracking.

[Features](#-features) • [Getting Started](#-getting-started) • [File Structure](#-file-structure) • [How It Works](#-how-it-works) • [Author](#-author)

</div>

---

## 📖 Overview

**SmartCafe** is a Python-based application designed to manage the daily operations of a cafe efficiently. It provides a simple command-line interface for staff to:

- Browse a structured menu of Beverages, Food, Desserts, and Snacks.
- Take customer orders with real-time price calculation.
- Persistently store all order data.
- Review order history and track total revenue.

The entire project follows an object-oriented design, making the code modular, readable, and easy to extend.

---

## ✨ Features

- **📋 Menu Management**: Pre-configured menu categories (Beverages, Food, Desserts, Snacks) with items and prices.
- **🧾 Order Processing**: Take customer orders, automatically calculate totals, and store them.
- **💾 Persistent Data Storage**: All order data and revenue are automatically saved in a JSON file (`database/cafe_data.json`) between sessions.
- **📊 Revenue Tracking**: View total accumulated revenue at any time.
- **🕒 Order History**: Review past orders directly within the application.
- **🏗️ Object-Oriented Design**: Clean architecture using Python classes for `MenuItem`, `Order`, and `CafeManager`, promoting maintainability and scalability.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.8 or higher** installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation & Execution

#### 1.  **Clone the repository**
```
    git clone https://github.com/92haroonkhalid/Smarf-Cafe.git
    cd SmartCafe
```
#### 2.Install dependencies (if any external packages are listed)
```
pip install -r requirements.txt
```

#### 3.Run the application
```
python -m smartcafe.main
```

---

## 📁 File Structure
The project follows a modular and standard Python package structure.
```
SmartCafe/
│
├── smartcafe/                  # Main application package
│   ├── __init__.py             # Makes 'smartcafe' a Python package
│   ├── main.py                 # Application entry point (contains the menu loop)
│   └── core_logic.py           # Core classes (MenuItem, Order, CafeManager)
│
├── Output Screenshots/
│   └── README.md               # Output Screenshots
│
├── database/                   # Data storage directory (auto-generated)
│   └── cafe_data.json          # Order and revenue data (not tracked by git)
│
├── .gitignore                  # Specifies intentionally untracked files
├── requirements.txt            # Python package dependencies
└── README.md                   # Project documentation (this file)
```
Note: The database/cafe_data.json file is automatically created when you first run the application and is intentionally excluded from version control via .gitignore.

---

## ⚙️ How It Works
### 1.Core Logic (smartcafe/core_logic.py):

- Defines the foundational MenuItem class with name and price attributes.

- Contains the Order class to hold a list of MenuItem objects, calculate the total, and generate a timestamp.

- Implements the CafeManager class, which orchestrates all operations: initializing the menu categorically, taking orders, saving/loading data to/from database/cafe_data.json, and viewing history/revenue.

### 2.Entry Point (smartcafe/main.py):

- Creates an instance of CafeManager.

- Presents a user-friendly, looped command-line menu, allowing the user to interact with all features until they choose to exit.

---

## 🛠️ Technology Stack
- Language: Python 3

- Data Storage: JSON

- Version Control: Git & GitHub

---

## 👤 Author
Haroon Khalid

GitHub: [@92haroonkhalid](https://github.com/92haroonkhalid)

---

## 📄 License
This project is open-source and available under the MIT License. See the ![License](https://img.shields.io/badge/license-MIT-green) file for more information (if added), or feel free to add one.
