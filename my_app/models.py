from django.db import models

# Create your models here.

class Position(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __int__(self):
        return self.id

class Comments(models.Model):
    cityName = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    emoji = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=300,blank=True,null=True)
    position = models.OneToOneField(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.cityName

