from django.db import models
# Create your models here.
class kolkatajobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    eligibility=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()


class blorejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    eligibility=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()

class chennaijobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    eligibility=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()

class punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    eligibility=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
