from django.db import models

# Create your models here.
class FakerData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    job = models.CharField(max_length=100)
    salary = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=100)