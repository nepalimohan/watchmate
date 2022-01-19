from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

# TYPE_CHOICES = (
#     ("Movies", "Movies"),
#     ("Web Series", "Web Series"),
# )

class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    # type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    
    def __str__(self):
        return self.name
