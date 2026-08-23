# 🖥️ Computer Shop Management System

A Django-based web application for managing computer shop operations — including user authentication, product management, a shopping cart system, and an admin dashboard.

---

## 📋 About the Project

This project simulates a real-world e-commerce workflow for a computer hardware/accessories shop. It allows customers to browse products, add them to a cart, and checkout, while giving admins full control over inventory and orders through a dedicated dashboard.

---

## ✨ Features

- 🔐 **User Authentication** — Register, log in, and manage customer accounts securely
- 🛒 **Cart System** — Add, update, and remove products from the shopping cart
- 📦 **Product Management** — Add, edit, and organize product listings
- 🧑‍💼 **Admin Dashboard** — Manage users, products, and orders from a central panel
- 💾 **SQLite Database** — Lightweight, file-based storage for easy setup

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- pip package manager

### Installation

```bash


# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
Computer-Shop/
├── manage.py
├── requirements.txt
├── shop_app/          # Core app: models, views, templates
├── static/            # CSS, JS, images
└── templates/         # HTML templates
```

> 💡 Update this to match your actual folder layout.

---




## 👩‍💻 Author

**Sayali** — [GitHub Profile](https://github.com/sayali2026)

⭐ Show Support If you like this project, give it a ⭐ on GitHub!

