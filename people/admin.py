from django.contrib import admin

from .models import Person


# /admin/ is a second way to see the same people_person rows.
# It reads and writes the database for you. It does not use the form on the home page.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "city", "created_at")
    search_fields = ("full_name", "email", "city")
