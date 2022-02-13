from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ("Special Fields", {'fields': ('is_author', 'special_user', 'thumbnail', 'description')}),
)

UserAdmin.list_display += ('is_author', 'is_special_user', 'date_joined')

admin.site.register(User, UserAdmin)