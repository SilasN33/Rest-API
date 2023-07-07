from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    plot = models.CharField(max_length=1000)
    year = models.DateField() 
    runtime = models.CharField(max_length=1000)
    genre = models.CharField(max_length=1000)
    director = models.CharField(max_length=1000)
    rating = models.FloatField()
    poster = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
class Series(models.Model):
    title = models.CharField(max_length=1000)
    plot = models.CharField(max_length=1000)
    year = models.DateField() 
    seasons = models.CharField(max_length=1000)
    genre = models.CharField(max_length=1000)
    writer = models.CharField(max_length=1000)
    rating = models.FloatField()
    poster = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.title
    


    

    




