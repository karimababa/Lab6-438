from django.db import models

class Team(models.Model):
    team_id = models.CharField(max_length=20)
    team_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    year_founded = models.CharField(max_length=4)


class Player(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    ppg = models.DecimalField(max_digits=2, decimal_places= 2)