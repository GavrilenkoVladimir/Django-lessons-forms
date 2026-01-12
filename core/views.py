from django.urls import reverse, reverse_lazy
from django.views import generic

from core.models import Person


class PersonListView(generic.ListView):
    model = Person


class PersonCreateView(generic.CreateView):
    model = Person
    fields = "__all__"
    success_url = reverse_lazy("core:person-list")
    template_name = "core/person_form.html"

