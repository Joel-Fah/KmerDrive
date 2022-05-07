import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/')
    bio = models.TextField()
    last_modified = models.DateField(auto_now=True)
    
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = os.path.join('../static/img/avatar.png')
        return url

    def __str__(self):
        return str(self.user)