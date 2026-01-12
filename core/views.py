from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from core.forms import PersonForm
from core.models import Person


class PersonListView(generic.ListView):
    model = Person


def person_create_view(request):
    context = {}
    form = PersonForm(request.POST or None)
    if form.is_valid():
        Person.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(reverse("core:person-list"))
    context["form"] = form
    return render(request, "core/person_form.html", context=context)


    # if request.method == "GET":
    #     context = {
    #         "form": PersonForm()
    #     }
    #     return render(
    #         request,
    #         "core/person_form.html",
    #         context=context
    #     )
    # elif request.method == "POST":
    #     form = PersonForm(request.POST)
    #     if form.is_valid():
    #         Person.objects.create(**form.cleaned_data)
    #         return HttpResponseRedirect(reverse("core:person-list"))
    #
    #     context = {
    #         "form": form,
    #     }
    #     return render(request, "core/person_form.html", context=context)

