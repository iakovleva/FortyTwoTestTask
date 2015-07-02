from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.CharField(max_length=150)
    skype = models.CharField(max_length=150)
