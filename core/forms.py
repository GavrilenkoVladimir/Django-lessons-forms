from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from core.models import Person


class PersonForm(forms.ModelForm):
    MIN_BIRTH_YEAR = 1900
    # birth_year = forms.IntegerField(
    #     required=True,
    #     validators=[MinValueValidator(MIN_BIRTH_YEAR)]
    # )

    class Meta:
        model = Person
        fields = ("full_name", "birth_year", "hobby", )

    # def clean_birth_year(self):
    #     birth_year = self.cleaned_data.get("birth_year")
    #     if birth_year < PersonForm.MIN_BIRTH_YEAR:
    #         raise ValidationError(f"Birth year must be at least {PersonForm.MIN_BIRTH_YEAR}.")
    #     return birth_year
