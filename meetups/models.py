from statistics import mode
from django.db import models


class Location(models.Model):   #here relationship mapping needed to map in Meetups model
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'

class Meetups(models.Model):
    title=models.CharField(max_length=200)
    location=models.CharField(max_length=200)

    #this django slugField adheres slug format
    slug=models.SlugField(unique=True)   
    description=models.TextField()
    image=models.ImageField(upload_to="images") 
    location=models.ForeignKey(Location,  on_delete=models.CASCADE)  #CASCADE in case we delete foreign key or data related with this table will be deleted automatically  not this only option and also you can use ondelete=SET_NULL


    def __str__(self):
        return f'{self.title} - {self.slug}'
