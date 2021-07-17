
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.fields import BigAutoField, BigIntegerField
# Create your models here.

class Station(models.Model):
    name = models.CharField(unique=True,max_length=100)
    pincode = models.IntegerField()
    def __str__(self) -> str:
        return self.name

class Edge(models.Model):
    source = models.ForeignKey(Station,on_delete=models.CASCADE, related_name="source")
    destination = models.ForeignKey(Station,on_delete=models.CASCADE, related_name="destination")
    duration = models.IntegerField()
    buses =  ArrayField(models.CharField(max_length = 10), blank=False)
    def __str__(self) -> str:
        return "From: " + self.source.name +".........To:  "+ self.destination.name
