from django import forms

class Student(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()
    rollno=forms.IntegerField()
    
