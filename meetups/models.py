from statistics import mode
from django.db import models

class Meetups(models.Model):
    title=models.CharField(max_length=200)
    location=models.CharField(max_length=200)

    #this django slugField adheres slug format
    slug=models.SlugField(unique=True)   
    description=models.TextField()
    image=models.ImageField(upload_to="images")


    def __str__(self):
        return f'{self.title} - {self.slug}'
