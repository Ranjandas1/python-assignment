# python-assignment

## Features

- Submit wheel inspection forms with metadata (form number, inspector, date)
- Store associated measurement data (diameter, profile, bearing size, etc.)
- One-to-One relationship between form and field data
- Filter forms by date range, inspector, and form number
- Clean, structured JSON responses for frontend or reporting tools
- RESTful API architecture using DRF ViewSets & Routers

---

## Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/Ranjandas1/python-assignment.git
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate (Windows: venv\Scripts\activate)
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup .env file

```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Api Endpoints

| Method | Endpoint                                                                                           | Description                 |
| ------ | -------------------------------------------------------------------------------------------------- | --------------------------- |
| GET    | `/form/wheelform/`                                                                                 | List all forms              |
| POST   | `/form/wheelform/`                                                                                 | Submit new form with fields |
| GET    | `/form/wheelform/?submittedBy=John&submittedDate_after=2025-07-01&submittedDate_before=2025-07-31` | Filter by metadata & date   |

---
