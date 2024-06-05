from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    isVerified = models.BooleanField(default=False)
    proofOfIncome = models.FileField(null=True, upload_to="documents/")
    governmentId = models.FileField(null=True, upload_to="documents/")
