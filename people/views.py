from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import PersonForm
from .models import Person


class PersonListView(View):
    """The home page.

    GET  shows the form and the people already saved.
    POST saves a new person, then sends the browser back to this page.
    """

    def get(self, request):
        # Opening the page, or arriving here after a redirect, is a GET.
        # Person.objects.all() reads every row: SELECT * FROM people_person.
        return render(
            request,
            "people/list.html",
            {
                "form": PersonForm(),  # empty form, ready for a new person
                "people": Person.objects.all(),
            },
        )

    def post(self, request):
        # The save form submits with method="post". request.POST is a
        # dictionary of the fields the user typed: full_name, email, ...
        form = PersonForm(request.POST)

        if form.is_valid():
            # is_valid() checks required fields and the unique email.
            # save() writes one row into the people_person SQL table.
            form.save()
            # "person_list" is not a method in this file. It is the name=
            # on the home URL in people/urls.py, which points at this class.
            # redirect() tells the browser to request that URL with GET,
            # and Django then calls PersonListView.get. A refresh will
            # not submit this form a second time.
            return redirect("person_list")

        # Validation failed. Show the same page, with the typed values
        # and the error messages still on the form. Nothing was saved.
        return render(
            request,
            "people/list.html",
            {
                "form": form,
                "people": Person.objects.all(),
            },
        )


class PersonDetailView(View):
    """One saved person. This page only reads, so it has a get method."""

    def get(self, request, pk):
        # pk comes from the URL, for example /3/. If no row has that id,
        # get_object_or_404 stops here and Django responds with 404.
        person = get_object_or_404(Person, pk=pk)
        return render(request, "people/detail.html", {"person": person})

