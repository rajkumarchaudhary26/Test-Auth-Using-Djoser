from django.contrib import admin
from django.db import models

from .constants import CLIENT, STAFF, USER_TYPES
from .models import User, Award, Profile
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email',]
    ordering = ['-date_joined']
    list_display = ('id', 'email', 'user_type', 'is_active', 'is_staff', 'is_superuser',)
    search_fields = ('email',)

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'year',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name_in_kanji', 'first_name_in_hiragana', 'first_name_in_english',)