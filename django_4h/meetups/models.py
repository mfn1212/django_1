from django.db import models

# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    desciption = models.TextField()
    image = models.ImageField(upload_to = 'images',null = True) 

    def __str__(self):
        return self.title

    