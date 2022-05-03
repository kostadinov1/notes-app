from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    image_url = models.URLField()
    content = models.TextField(blank=False, null=False)

