from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    population = models.IntegerField()
    founder = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)


    def __str__(self):
        return self.name
