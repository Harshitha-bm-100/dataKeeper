from django.urls import path

from . import views

# as_view() turns the class into the function Django calls for a request.
# Django then picks view.get or view.post from the request method.
urlpatterns = [
    path("", views.PersonListView.as_view(), name="person_list"),
    path("<int:pk>/", views.PersonDetailView.as_view(), name="person_detail"),
]
