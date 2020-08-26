from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(max_length=1000)
    date_of_birth = models.DateField

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(max_length=1000)
    date_of_birth = models.DateField

    def __str__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(max_length=1000)
    date_of_birth = models.DateField

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=100)
    production_year = models.IntegerField(max_length=4)
    length = models.TimeField
    release_date = models.DateField
    description = models.TextField(max_length=500)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    trailer = models.CharField(max_length=150)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    writers = models.ManyToManyField(Writer)

    def __str__(self):
        return f"{self.name} ({self.production_year})"
        

class Discussion(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}'s discussion about {self.parent_movie}"

class Comment(models.Model):
    text = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}'s comment on {self.parent_discussion}"
    
        