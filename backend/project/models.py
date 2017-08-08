from django.db import models

# Create your models here.

class IdeasModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=256)

class PlayersModel(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class GameModel(models.Model):
    username = models.CharField(max_length=50, default="")

class WinnerModel(models.Model):
    username = models.CharField(max_length=50, default="")