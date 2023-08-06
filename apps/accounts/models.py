from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='teams')

    def __str__(self):
        return self.name