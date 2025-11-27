from django.contrib import admin

# Register your models here.
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email')

    list_display_links = ('id','username','email')

admin.site.register(CustomUser,CustomUserAdmin)