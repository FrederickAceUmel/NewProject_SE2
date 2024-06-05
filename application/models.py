from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    isVerified = models.BooleanField(default=False)
    proofOfIncome = models.FileField(null=True, upload_to="documents/")
    governmentId = models.FileField(null=True, upload_to="documents/")
=======

# Create your models here.
class UserProfile(models.Model):
    new_field = models.CharField(max_length=140, default='SOME STRING')
    image_field = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
>>>>>>> Cash-Assistance-Module
