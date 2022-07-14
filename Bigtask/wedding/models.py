from django.db import models

# Create your models here.

class workview(models.Model):
    Title = models.CharField(max_length=50)
    Desc = models.CharField(max_length=500, default = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia')
    link = models.URLField(default='http://127.0.0.1:8000/')
    #date = models.CharField(max_length=10)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.Title

class MostPopular(models.Model):
    Title = models.CharField(max_length=50)
    Desc = models.CharField(max_length=500, default = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia')
    link = models.URLField(default='http://127.0.0.1:8000/')
    #date = models.CharField(max_length=10)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.Title

class LatestWork(models.Model):
    Title = models.CharField(max_length=50)
    Desc = models.CharField(max_length=500, default = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia')
    link = models.URLField(default='http://127.0.0.1:8000/')
    #date = models.CharField(max_length=10)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.Title

class OurFavourites(models.Model):
    Title = models.CharField(max_length=50)
    Desc = models.CharField(max_length=500, default = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia')
    link = models.URLField(default='http://127.0.0.1:8000/')
    #date = models.CharField(max_length=10)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.Title

class BehindTheScenes(models.Model):
    Title = models.CharField(max_length=50)
    Desc = models.CharField(max_length=500, default = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia')
    link = models.URLField(default='http://127.0.0.1:8000/')
    #date = models.CharField(max_length=10)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.Title