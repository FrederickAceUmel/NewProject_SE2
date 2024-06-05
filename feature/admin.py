from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import CashAssistance

# Register your models here.
@admin.register(CashAssistance)
class CashAssistanceAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'view_user_profile')

    @admin.display(ordering='userprofile__username', description='Username')
    def get_username(self, obj):
        return obj.user_profile.user.username
    
    def view_user_profile(self, obj):
        url = reverse("admin:application_userprofile_change", args=[obj.user_profile.id])
        return format_html('<a href="{}">User Profile</a>', url)

    view_user_profile.short_description = "User Profile"
