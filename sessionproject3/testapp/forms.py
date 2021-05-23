from django import forms

class Additemform(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()
