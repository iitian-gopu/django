from django import forms

class nameform(forms.Form):
    name = forms.CharField()

# Create your tests here.
class ageform(forms.Form):
    age = forms.CharField()

class gfform(forms.Form):
    gf = forms.CharField()
