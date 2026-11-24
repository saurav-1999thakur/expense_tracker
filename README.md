<<<<<<< HEAD
# Expense Tracker Web Application

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

A modern, secure, and intuitive web application designed to help individuals take full control of their personal finances. Built with **Python**, **Flask**, and **SQLAlchemy**, this application enables users to log daily expenses, categorize transactions, track monthly spending patterns, and maintain financial clarity through a clean, responsive dashboard.

---

## Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Routes & Endpoints](#-routes--endpoints)
- [Future Roadmap](#-future-roadmap)
- [License](#-license)

---

## Overview

Managing personal expenses is essential for achieving financial freedom. **Expense Tracker** simplifies budgeting by providing a centralized platform to record, inspect, and analyze personal expenditures. Each registered user gets an isolated financial workspace where they can monitor budgets against monthly income, view category-wise breakdowns, and manage individual transactions seamlessly.

---

## Key Features

### 1. Authentication & Security
- **User Registration & Validation**: Form validation with checks for duplicate emails and usernames, phone number formats, and password confirmation.
- **Secure Password Hashing**: Utilizes `werkzeug.security` (`generate_password_hash` and `check_password_hash`) to ensure credentials are encrypted.
- **Session Management**: Session-based login control guarding sensitive endpoints with access-control helpers.

### 2. Expense Management (CRUD)
- **Create**: Quickly add expenses with amounts, descriptions, and predefined categories.
- **Read**: View chronological transaction logs and drill down into individual expense detail views.
- **Update**: Edit existing expense descriptions, amounts, or categories with pre-filled forms.
- **Delete**: Remove transactions with user ownership verification and client confirmation alerts.

### 3. Interactive Dashboard & Analytics
- **Financial Summary Cards**: Real-time display of **Total Balance**, **Monthly Income**, and **Total Monthly Spending**.
- **Category Breakdown**: Automatically calculates spending distributions across categories (Food, Transport, Bills, Shopping, Health, Entertainment, Education, etc.).
- **Quick Actions**: One-click shortcuts to record expenses and access transaction histories.

### 4. Responsive UI & Clean UX
- Modern, clean aesthetic built with custom CSS flexbox/grid layouts.
- Toast-style flash message alerts for real-time user feedback.
- Integrated search and category filters on the transaction history page.

---

## Tech Stack

- **Backend**: [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/)
- **Database & ORM**: [SQLite](https://www.sqlite.org/), [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- **Forms & Validation**: [Flask-WTF](https://flask-wtf.readthedocs.io/), [WTForms](https://wtforms.readthedocs.io/), `email-validator`
- **Security**: [Werkzeug](https://werkzeug.palletsprojects.com/)
- **Frontend**: HTML5, Modern CSS3, JavaScript (Vanilla)

---


## Project Structure

```text
expense_tracker/
│
├── app.py                  # Core application entrypoint, routes, and DB models
├── forms.py                # WTForms definitions (Registration, Login, Expense)
├── create_table.py         # Utility script to initialize the SQLite database
├── apply.py                # API/helper routes
├── instance/
│   └── expenses.db         # SQLite database file (created after init)
├── static/
│   ├── css/
│   │   └── style.css       # Custom styles and dashboard layout rules
│   └── js/
│       └── main.js        # Client-side behaviors and notifications
├── templates/
│   ├── base.html           # Base layout with navigation and flash messages
│   ├── home.html           # Landing page with hero banner & features
│   ├── dashboard.html      # Overview dashboard with analytics & summary cards
│   ├── expenses.html       # Tabular view of all user transactions with filters
│   ├── add_expense.html    # Add new expense transaction form
│   ├── edit_expense.html   # Update existing transaction form
│   ├── single_expense.html # Detailed individual transaction view
│   ├── login.html          # User authentication login page
│   └── register.html       # New user registration page
└── README.md               # Project documentation
```

---

## Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed on your system:
```bash
python --version
```

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/expense_tracker.git
   cd expense_tracker
   ```

2. **Create and activate a virtual environment**:
   - **Windows**:
     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install required dependencies**:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-WTF email-validator
   ```

4. **Initialize the Database**:
   Run the database initialization script to create the necessary tables:
   ```bash
   python create_table.py
   ```

5. **Run the Flask Development Server**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Routes & Endpoints

| Route | Methods | Description | Protected |
| :--- | :--- | :--- | :---: |
| `/` | `GET` | Home landing page with app highlights | No |
| `/register` | `GET`, `POST` | New user account registration | No |
| `/login` | `GET`, `POST` | User authentication and session creation | No |
| `/logout` | `GET` | Clear session and return to home | Yes |
| `/dashboard` | `GET` | Metrics overview (balance, income, expenses) | Yes |
| `/expenses` | `GET` | View list of all transactions with search & filter | Yes |
| `/add-expense` | `GET`, `POST` | Form to create a new expense record | Yes |
| `/expense/<id>` | `GET` | Inspect details of a single transaction | Yes |
| `/expense/<id>/edit` | `GET`, `POST` | Edit existing expense details | Yes |
| `/expense/<id>/delete`| `POST` | Delete a specific transaction | Yes |

---

## Future Roadmap

- [ ] Interactive dynamic charts using Chart.js or ApexCharts
- [ ] Export transactions to CSV / Excel / PDF
- [ ] Customizable monthly budget limits with threshold alerts
- [ ] Support for multiple currencies and recurring bills
- [ ] RESTful API endpoints with JWT authentication

---

## License

This project is open-source and available under the [MIT License](LICENSE).
=======

>>>>>>> origin/main
