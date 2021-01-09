from django.db import models


# Create your models here.
class TestObject(models.Model):
    name = models.TextField()
    value = models.TextField()
