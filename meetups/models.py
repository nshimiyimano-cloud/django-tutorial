from statistics import mode
from django.db import models

class Meetups(models.Model):
    title=models.CharField(max_length=200)

    #this django slugField adheres slug format
    slug=models.SlugField(unique=True)   
    description=models.TextField()
