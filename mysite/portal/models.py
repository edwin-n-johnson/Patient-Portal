from django.db import models

# Create your models here.
class User(models.Model):
    username  = models.CharField(max_length=256)
    firstname = models.CharField(max_length=256)
    lastname  = models.CharField(max_length=256)
