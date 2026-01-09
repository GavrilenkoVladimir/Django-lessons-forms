from django.urls import path

from core.views import PersonListView, person_create_view

app_name = "core"
urlpatterns = [
    path("people/", PersonListView.as_view(), name="person-list"),
    path("people/create/", person_create_view, name="person-create"),
]