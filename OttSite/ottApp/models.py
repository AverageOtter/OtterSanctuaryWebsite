from enum import unique
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class species(models.Model):
    speciesname = models.CharField(max_length=150, unique=TRUE)
    scientificname = models.CharField(max_length=150, unique=TRUE)
    healthyweightmin = models.FloatField()  # in kg
    healthyweightmax = models.FloatField()  # in kg
    origin = models.CharField(max_length=150)
    land = models.BooleanField()

    # To make admin page not show up as Object 1-13
    def __str__(self):
        return "%s" % self.speciesname


class onsite(models.Model):
    name = models.CharField(max_length=30, unique=TRUE)
    SEX_CHOICES = [("M", "Male"), ("F", "Female")]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.SmallIntegerField()
    weight = models.FloatField()  # in kg
    breakfast = models.TimeField()
    lunch = models.TimeField()
    dinner = models.TimeField()
    snack = models.CharField(max_length=150, blank=TRUE)
    species = models.ForeignKey(species, on_delete=models.CASCADE)
    
    # To make admin page not show up as Object 1-13
    def __str__(self):
        return "%s the %s" %(self.name, self.species.speciesname)


