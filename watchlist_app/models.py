from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
