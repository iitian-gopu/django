from django import forms

class feedback(forms.Form):
    name = forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

def clean_name(self):
    inputname=self.cleaned_data['name']
    if len(inputname)<=4:
        raise forms.ValidationError(len>=4)
    return inputname
