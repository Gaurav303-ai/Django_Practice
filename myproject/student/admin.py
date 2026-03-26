from django.contrib import admin
from .models import Profile
# Register your models here.


# class ProfileAdmin(admin.ModelAdmin):
#     list_display=('name','city','email','roll')
    
# admin.site.register(Profile, ProfileAdmin)

#you also use this way
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('name','city','email','roll')