from django.db import models


class Person(models.Model):
    """One row in the SQL table named people_person.

    Django builds that table name from the app name (people) and this
    class name in lowercase (person). You do not write CREATE TABLE
    yourself. `makemigrations` and `migrate` do that from the fields below.

    Each field is one column:
      id          added automatically, the primary key
      full_name   text, required, at most 120 characters
      email       text, required, no two rows may share it
      phone       text, optional (blank=True allows "")
      city        text, optional
      notes       long text, optional
      created_at  date and time, filled in when the row is inserted
    """

    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Default order for Person.objects.all(): alphabetical by name.
        ordering = ["full_name"]

    def __str__(self):
        # What print(person) and the admin list show.
        return self.full_name
