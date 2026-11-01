# Data Keeper

Save a person's details in a SQLite database and look them up again in the browser.

## Description

Data Keeper is a small Django web app for storing people. On the home page you enter a name, email, and optional phone, city, and notes. Django checks the form and, if it is valid, writes one row to a local SQLite database. The same page lists everyone already saved, in alphabetical order by name. Click a name to open that one record. A missing id shows a 404 page. The same records are also available in Django admin after you create an admin login.

Name and email are required. The email must look like an email address, and two people cannot share one. Phone, city, and notes can be left blank.

## Getting Started

### Dependencies

- Python 3
- pip
- Git

Django 6.1.2 is installed from `requirements.txt`. SQLite comes with Python, so you do not install a separate database. The app runs on macOS, Linux, and Windows.

### Installing

Clone the repository and install its dependencies inside a virtual environment.

macOS and Linux:

```bash
git clone https://github.com/Harshitha-bm-100/dataKeeper.git
cd dataKeeper
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Windows:

```bash
git clone https://github.com/Harshitha-bm-100/dataKeeper.git
cd dataKeeper
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

`migrate` creates `db.sqlite3` in the project folder. That file is local. It is listed in `.gitignore`, so it is not part of the clone. No project files need to be edited before the first run.

### Executing program

1. Activate the virtual environment if the terminal does not already show `(.venv)`.
2. Start the server:

```bash
python manage.py runserver
```

3. Open http://127.0.0.1:8000/.
4. Fill in the form and press Save.
5. Click a name in the list to open that record.

Optional admin site:

```bash
python manage.py createsuperuser
```

Then open http://127.0.0.1:8000/admin/ and sign in with that account.

Stop the server with Ctrl+C.

## Authors

- [Harshitha-bm-100](https://github.com/Harshitha-bm-100)

## Version History

- 0.1
  - Initial release
