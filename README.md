# Data Keeper

Data Keeper stores people in a SQLite database and shows them on a web page. You type a person's details, Django saves one row, and the home page lists every row. Click a name to see that one record.

The database file is `db.sqlite3` in this folder. The table is `people_person`.

## What the pages do

**Home page, `/`**

- GET (opening the page) reads every row with `Person.objects.all()` and shows them under "Everyone saved", in alphabetical order by name. It also shows an empty form.
- POST (pressing Save) checks the form. If the name and email are present and the email is not already saved, `form.save()` inserts one row. The browser is then sent back to `/` with a GET, so a refresh does not save the same person twice.
- If the form is invalid, the page stays put, the row is not written, and the error is shown on the field. An empty name, an empty email, a badly shaped email, or a duplicate email is invalid. Phone, city, and notes may be left blank.

**One person, `/<id>/`**

GET only. The number in the URL is the row's `id`. Example: `/3/` loads the person whose `id` is 3. A missing id returns a 404 page. The page shows name, email, phone, city, notes, and the time the row was saved. "Back to everyone" returns to `/`.

**Admin, `/admin/`**

A second view of the same table. It is empty until you create a login with `python manage.py createsuperuser`.

## What is stored

| Column | Required | Rule |
| --- | --- | --- |
| `id` | yes | Number created by the database. This is the number in `/3/`. |
| `full_name` | yes | Text, at most 120 characters. |
| `email` | yes | Must look like an email. Two people cannot share one. |
| `phone` | no | Text, at most 30 characters. |
| `city` | no | Text, at most 80 characters. |
| `notes` | no | Longer text. |
| `created_at` | yes | Date and time filled in when the row is inserted. |

## Where that behavior lives

| File | Job |
| --- | --- |
| `people/models.py` | Describes the columns. |
| `people/forms.py` | Builds the Save form from those columns and checks them. |
| `people/views.py` | `PersonListView.get` shows the list. `PersonListView.post` saves. `PersonDetailView.get` shows one person. |
| `people/urls.py` | `/` is named `person_list`. `/<id>/` is named `person_detail`. `redirect("person_list")` means "go to `/`", not "call a method named person_list". |
| `config/urls.py` | Sends `/` into `people/urls.py` and `/admin/` to Django's admin. |
| `config/settings.py` | Turns the app on and points the database at `db.sqlite3`. |
| `people/templates/people/list.html` | The home page. |
| `people/templates/people/detail.html` | The one-person page. |
| `people/migrations/0001_initial.py` | The saved instructions that create the table. |

## Run it

From this folder:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/.

`source .venv/bin/activate` turns on this project's virtual environment. The prompt shows `(.venv)`, and `python` then means the Python that has Django installed.

## Migrate after you change the model

Do this when you add, remove, or rename a field in `people/models.py`. Changing a template or a view does not need a migration.

```bash
source .venv/bin/activate
python manage.py makemigrations
python manage.py migrate
```

`makemigrations` compares `models.py` with the last migration file and writes a new file in `people/migrations/`. That file is code, and it belongs on GitHub.

`migrate` runs any migration files that have not been applied yet and updates `db.sqlite3`. The database file stays on your machine. It is listed in `.gitignore`.

If `makemigrations` prints "No changes detected", the model matches the migrations already on disk.

## Push the code to GitHub

This folder is not a git repository yet. Run these commands from `/Users/harry/Documents/dataKeeper` once:

```bash
git init
git add .
git status
git commit -m "Add Data Keeper."
gh repo create dataKeeper --source=. --private --push
```

`git status` before the commit should not list `.venv/` or `db.sqlite3`. Those are ignored on purpose. If either appears, do not commit it.

Later, after more edits:

```bash
cd /Users/harry/Documents/dataKeeper
git status
git add .
git commit -m "Describe what you changed."
git push
```

If you also changed `people/models.py`, run `makemigrations` first and include the new file under `people/migrations/` in that commit. Someone who clones the repository then runs `python manage.py migrate` to build their own empty database.
