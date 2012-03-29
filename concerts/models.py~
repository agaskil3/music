from django.contrib.auth.models import User, UserManager 
from django.db import models


class Genre(models.Model):
    genre= models.CharField(max_length=255)
    genre_slug= models.SlugField()
    def __unicode__(self):
        return self.genre

class City(models.Model):
    city= models.CharField(max_length=255)
    city_slug= models.SlugField()
    def __unicode__(self):
        return self.city

class State(models.Model):
    state= models.CharField(max_length=255)
    state_slug= models.SlugField()
    def __unicode__(self):
        return self.state

class Zipcode(models.Model):
    zipcode= models.CharField(max_length=255)
    zipcode_slug= models.SlugField()
    def __unicode__(self):
        return self.zipcode

class Artist(models.Model):
    artist = models.CharField(max_length=225)
    artist_slug= models.SlugField()
    bio = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Genre) 
    def __unicode__(self):
        return self.artist 

class Location(models.Model):
    title = models.CharField(max_length=225)
    title_slug= models.SlugField()
    address = models.CharField(max_length=225)
    city = models.ForeignKey(City)
    state = models.ForeignKey(State)
    zipcode = models.ForeignKey(Zipcode)
    description = models.TextField()
    def __unicode__(self):
        return self.location

class Event(models.Model):
    title = models.CharField(max_length=255)
    title_slug = models.SlugField()
    main_acts = models.ManyToManyField(Artist, related_name="main_set")
    opening_acts = models.ManyToManyField(Artist, related_name="opening_set", blank=True, null=True)
    def __unicode__(self):
        return self.title

class Photo(models.Model):
    photo = models.CharField(max_length=225)
    photo_slug = models.SlugField()
    user = models.ForeignKey(User)
    show = models.CharField(max_length=225)
    date = models.DateField(max_length=225)
    caption = models.TextField()
    photo = models.ImageField(upload_to="photos/")
    def __unicode__(self):
        return self.photo     
