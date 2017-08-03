from django.db import models

# Create your models here.

class ExampleModel(models.Model):
    firstname = models.CharField(max_length=50)

class LinkExample(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.ForeignKey(ExampleModel, on_delete=models.CASCADE)