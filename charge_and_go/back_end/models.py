from django.db import models


# Create your models here.
class userAccount(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ("FEMALE", "Female"),
        ("MALE", "Male"),
        ("OTHER", "Other"),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)