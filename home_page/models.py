from django.db import models

class ProfilePicture(models.Model):
    image = models.ImageField(upload_to='images/', default='null', blank=True)
    
    def __str__(self):
        return "Profile Picture"
