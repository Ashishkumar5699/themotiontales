from django.db import models

# Create your models here.

class workview(models.Model):
    name = models.CharField(max_length=50)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.name

class MostPopular(models.Model):
    name = models.CharField(max_length=50)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.name

class LatestWork(models.Model):
    name = models.CharField(max_length=50)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.name

class OurFavourites(models.Model):
    name = models.CharField(max_length=50)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.name

class BehindTheScenes(models.Model):
    name = models.CharField(max_length=50)
    image_file = models.FileField(upload_to='images', default = "")

    def __str__(self):
        return self.name