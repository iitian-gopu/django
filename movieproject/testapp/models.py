from django.db import models

# Create your models here.
class movie(models.Model):
    rdate=models.DateField()
    moviename = models.CharField(max_length=200)
    hero=models.CharField(max_length=200)
    heroine=models.CharField(max_length=200)
    rating=models.IntegerField()
    
