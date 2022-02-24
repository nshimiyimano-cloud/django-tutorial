from enum import unique
from statistics import mode
from typing_extensions import Self
from django.db import models


class Location(models.Model):   #here relationship mapping needed to map in Meetups model
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email=models.EmailField(unique=True)
    #meetups=models.ManyToManyField(Meetups) and to do taht here again not necesary in Meetups model its enough becouse behind the scene django do this for us

    def __str__(self):
        return self.email 

class Meetups(models.Model):
    title=models.CharField(max_length=200)
    organizer_email=models.EmailField()
    date=models.DateField()
    #location=models.CharField(max_length=200) no we have wrapped this in location

    #this django slugField adheres slug format
    slug=models.SlugField(unique=True)   
    description=models.TextField()
    image=models.ImageField(upload_to="images") 
    location=models.ForeignKey(Location,  on_delete=models.CASCADE)  #CASCADE in case we delete foreign key or data related with this table will be deleted automatically  not this only option and also you can use ondelete=SET_NULL this is onetomany
    participant=models.ManyToManyField(Participant, blank=True,null=True)  #addition blank makes here in Meetups form field  even not be filled no problem as optional and null as nullable in db eg on dashboard even we if we haven't added participant not affect  because blank allowed in filling form so we allow to store null value in database


    def __str__(self):
        return f'{self.title} - {self.slug}'
