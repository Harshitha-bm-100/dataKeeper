from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    """The HTML form for creating a Person.

    ModelForm reads the fields from the Person model, so the form and
    the database columns stay in step. It also checks the rules declared
    on the model, such as "email is required" and "email must be unique."
    """

    class Meta:
        model = Person
        # created_at is left out on purpose. The database fills that in.
        fields = ["full_name", "email", "phone", "city", "notes"]
        # widgets only change how the input looks in the browser.
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone"}),
            "city": forms.TextInput(attrs={"placeholder": "City"}),
            "notes": forms.Textarea(attrs={"rows": 3, "placeholder": "Notes"}),
        }
