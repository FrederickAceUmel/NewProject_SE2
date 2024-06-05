from django.contrib import admin
<<<<<<< HEAD
from application.models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_last_name', 'get_first_name', 'isVerified')
    list_filter = ('isVerified',)


    @admin.display(ordering='user__username', description='Username')
    def get_username(self, obj):
        return obj.user.username
    

    @admin.display(ordering='user__last_name', description='Last Name')
    def get_last_name(self, obj):
        return obj.user.last_name
    

    @admin.display(ordering='user__first_name', description='First Name')
    def get_first_name(self, obj):
        return obj.user.first_name
=======

# Register your models here.
>>>>>>> Cash-Assistance-Module
