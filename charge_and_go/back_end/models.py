from django.db import models


# Create your models here.
class userAccount(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.IntegerField() #change later
