from django.shortcuts import render
from django.views import generic

from core.models import Person


class PersonListView(generic.ListView):
    model = Person


def person_create_view(request):
    return render(request, "core/person_list.html")
