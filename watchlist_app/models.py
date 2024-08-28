from django.db import models

# Create your models here.
class StreamPlatforms(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
class Watchlists(models.Model):
    name= models.CharField(max_length=50)
    description= models.CharField(max_length=200)
    platform= models.ForeignKey(StreamPlatforms, on_delete=models.CASCADE, related_name= 'watchlist')
    active= models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name