""" admin for blat """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Blat, Profile

# Register your models here.
class BlatAdmin(admin.ModelAdmin):
    """blat admin model to edit from admin site"""
    list_display = ['text', 'via', 'total_likes']
    list_filter = ['created_on']
    search_fields = ['text']

class ProfileInline(admin.StackedInline):
    """Profile Model to be edited on admin interface"""
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):# pylint: disable=function-redefined
    """ProfileInline added to inlines for UserAdmin"""
    inlines = (ProfileInline,)


admin.site.register(Blat, BlatAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
