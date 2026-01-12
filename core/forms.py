from django import forms

class PersonForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    birth_year = forms.IntegerField()
    hobby = forms.CharField(max_length=255, required=False)