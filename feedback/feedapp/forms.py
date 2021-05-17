from django import forms
from django.core import validators

class feedback(forms.Form):
    name = forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
          print("Total Vlidation")
          cleaned_data= super().clean()
          bot_handler_value=cleaned_data['bot_handler']
          if len(bot_handler_value)>0:
              raise forms.ValidationError("Thanksbots")
