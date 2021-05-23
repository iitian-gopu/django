from django.db import models

# Create your models here.
class filtermodel(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    dept = models.CharField(max_length=200)
    date = models.DateField(max_length=200)
