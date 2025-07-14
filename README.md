# python-assignment

## 🧰 Features

- Submit wheel inspection forms with metadata (form number, inspector, date)
- Store associated measurement data (diameter, profile, bearing size, etc.)
- One-to-One relationship between form and field data
- Filter forms by date range, inspector, and form number
- Clean, structured JSON responses for frontend or reporting tools
- RESTful API architecture using DRF ViewSets & Routers

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

git clone

### 2. Set Up Virtual Environment

```bash
python -m venv env
source env/bin/activate (Windows: env\Scripts\activate)
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup env file

### 4. Apply Migrations

```bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
```
