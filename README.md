# Expense Tracker – Backend

Django REST API for tracking personal expenses, with token-based authentication and a server-rendered dashboard.

The frontend client is available at [ExpenseTracker-Frontend](https://github.com/ShahadAlkamli/ExpenseTracker-Frontend).

---

## Features

- REST API for creating, reading, updating, and deleting transactions
- Running balance with separate income and expense totals
- Token-based authentication
- Session-based login and logout using Django's built-in auth views
- Protected dashboard rendered with Django templates
- Test suite covering the model and all API endpoints

---

## Tech Stack

- **Django 5** — web framework
- **Django REST Framework** — API layer
- **SQLite** — database
- **Vanilla JavaScript** — dashboard interactivity

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
│     ├── templates/         # Dashboard and login templates
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

## License

This repository is provided for academic and learning purposes.```

### 3️⃣ Start the server
```bash
python manage.py runserver
```

The backend will run at:

```
http://127.0.0.1:8000/
```

---

## 🔗 Connecting to the Frontend (Optional)

If using the Vue frontend:

1. Start this Django server first  
2. Enable CORS if necessary  
3. Update your Vue app to send requests to:

```
http://127.0.0.1:8000/api/
```

---

## 📦 Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📜 License
This project is part of the **Expense Tracker Full-Stack Application**.
