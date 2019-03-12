from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class UsersList(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'role']
    list_filter = ['role']
