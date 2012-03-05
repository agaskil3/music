from django.db import models

class Genre(models.Model):
    genre= models.CharField(max_length=255)
    genre_slug= models.SlugField()
    def __unicode__(self):
        return self.genre

class Artist(models.Model):
    
