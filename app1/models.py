from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField()
    
    def __str__(self):
        return self.title