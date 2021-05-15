from home_page import models
from django.contrib import admin
from home_page.models import ProfilePicture

class ProfilePictureAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProfilePicture, ProfilePictureAdmin)
