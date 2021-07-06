
from django.contrib.postgres.fields import ArrayField
from django.db import models
# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Edge(models.Model):
    source = models.ForeignKey(Station,on_delete=models.CASCADE, related_name="source")
    destination = models.ForeignKey(Station,on_delete=models.CASCADE, related_name="destination")
    duration = models.IntegerField()
    buses =  ArrayField(models.IntegerField(), blank=True)
    def __str__(self) -> str:
        return "From: " + self.source.name +".........To:  "+ self.destination.name
