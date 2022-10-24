from django.db import models

# Create your models here.


class Participant (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)


class Location (models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    desciption = models.TextField()
    image = models.ImageField(upload_to='images', null=True)
    address = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return self.title
