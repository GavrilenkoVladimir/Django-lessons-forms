from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from core.models import Person


class PersonListView(generic.ListView):
    model = Person


def person_create_view(request):
    if request.method == "GET":
        return render(request, "core/person_form.html")
    elif request.method == "POST":
        full_name = request.POST.get("full_name")
        birth_year = request.POST.get("birth_year")
        if full_name and birth_year:
            Person.objects.create(
                full_name=full_name,
                birth_year=birth_year, )
            return HttpResponseRedirect(reverse("core:person-list"))

        else:
            context = {
                "error": "Please, provide all information"
            }
            return render(request, "core/person_form.html", context=context)

