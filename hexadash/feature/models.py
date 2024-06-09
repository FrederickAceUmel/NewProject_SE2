from django.db import models
from application.models import UserProfile

# Create your models here.
class CashAssistance(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    contact = models.TextField(null=True)
    birthday = models.DateField(null=True)
    address = models.TextField(null=True)
    proof_of_residency = models.FileField(null=True, upload_to="documents/")
    household_member_count = models.IntegerField(null=True)
    special_categories = models.JSONField(null=True)
    employment_status = models.TextField(null=True)
    monthly_income = models.BigIntegerField(null=True)
    government_aid = models.BooleanField(null=True)
    income_verification = models.FileField(null=True, upload_to="documents/")
    reason = models.JSONField(null=True)
    other_proof = models.FileField(null=True, upload_to="documents/")
    is_approved = models.BooleanField(default=False)