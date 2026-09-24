# Expense Tracker – Django

A full-stack expense tracking web application built with Django, featuring a REST API, token-based authentication, and a server-rendered dashboard.

---

## Features

- REST API for creating, reading, updating, and deleting transactions
- Running balance with separate income and expense totals
- Token-based authentication for API access
- Session-based login and logout using Django's built-in auth views
- Protected single-page dashboard rendered with Django templates
- Test suite covering the model and all API endpoints

---

## Tech Stack

- **Django 5** — web framework
- **Django REST Framework** — API layer
- **SQLite** — database
- **Django templates + vanilla JavaScript** — frontend

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/transactions/` | List all transactions |
| `POST` | `/api/transactions/` | Create a transaction |
| `GET` | `/api/transactions/<id>/` | Retrieve a transaction |
| `PUT` / `PATCH` | `/api/transactions/<id>/` | Update a transaction |
| `DELETE` | `/api/transactions/<id>/` | Delete a transaction |
| `POST` | `/accounts/login/` | Log in |
| `POST` | `/accounts/logout/` | Log out |

---

## Data Model

```python
Transaction
├── text    CharField(max_length=255)
└── amount  DecimalField(max_digits=10, decimal_places=2)
```

Positive amounts represent income, negative amounts represent expenses. The dashboard derives the running balance, total income, and total expenses from these values.

A single-table schema was chosen deliberately: the data requirements are straightforward, and avoiding unnecessary relations keeps queries simple and the application easy to maintain.

---

## Project Structure

```
├── ExpenseTracker/          # Project settings and root URLs
├── myapp/
│     ├── models.py          # Transaction model
│     ├── views.py           # API views and dashboard
│     ├── serializers.py     # DRF serializers
│     ├── urls.py            # URL routing
│     ├── admin.py           # Admin registration
│     ├── tests.py           # Test suite
│     ├── templates/         # Dashboard and login pages
│     └── static/            # CSS and JavaScript
├── manage.py
└── README.md
```

---

## Setup

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install django djangorestframework
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Create a superuser

```bash
python manage.py createsuperuser
```

### 5. Run the server

```bash
python manage.py runserver
```

The dashboard is available at `http://127.0.0.1:8000/` and the API at `http://127.0.0.1:8000/api/transactions/`.

---

## Tests

```bash
python manage.py test
```

The suite covers model creation and all CRUD endpoints.

---

## Related

An earlier implementation of the same concept built with Vue 3, using browser storage instead of a database: [ExpenseTracker-Vue](https://github.com/ShahadAlkamli/ExpenseTracker-Vue).

---

## License

This repository is provided for academic and learning purposes.
