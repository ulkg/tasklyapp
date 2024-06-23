import os

from django.db import models
from django.contrib.auth.models import User

from django.utils.deconstruct import deconstructible

# decorator: allow django to create a migration (ORM)
@deconstructible
class GenerateProfileImagePath(object):
    
    def __init__(self):
        pass
    
    def __call__(self, instance, filename):
        extension = filename.split('.')[-1]
        # f string feature: embedded variables into string
        path = f'media/accounts/{instance.user.id}'
        name = f'profile_image.{extension}'
        return os.path.join(path, name)

user_profile_image_path = GenerateProfileImagePath()

# inherit from models.Model
class Profile(models.Model):
    # one to one relationship, delete profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_profile_image_path, blank=True, null=True)
    
    # string representation of mode, used in admin panel
    def __str__(self):
        return f'{self.user.username}\'s Profile'
