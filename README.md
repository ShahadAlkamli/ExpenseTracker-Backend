# Expense Tracker – Backend (Django)

This is the backend web application for the Expense Tracker project.  
It provides the database, API logic, and server-side functionality used by the frontend app.

---

## 🚀 Features
- Built with **Django**
- Stores expenses in a database
- CRUD (Create, Read, Update, Delete) operations for expenses
- REST-style API endpoints (if using Django REST Framework)
- Can connect to the Vue.js frontend

---

## 🧰 Tech Stack
- **Python 3**
- **Django**
- **SQLite** (default database)
- **Django REST Framework** (optional)

---

## 📁 Project Structure
```
ExpenseTracker/
    settings.py
    urls.py
    models.py
    views.py
db.sqlite3
manage.py
```

---

## ▶️ Run the Project Locally

### 1️⃣ Install dependencies
(If you have a requirements.txt file)
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install django
```

### 2️⃣ Apply database migrations
```bash
python manage.py migrate
```

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
