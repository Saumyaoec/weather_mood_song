from django.db import models

class UserInput(models.Model):
    mood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
