from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BaseUser


class BaseUserAdmin(UserAdmin):
  list_display = (
    'username',
    'email',
    'date_of_birth',
    'is_staff',
    'is_active',
    'date_joined',
  )
  list_filter = (
    'location',
    'date_of_birth',
    'is_staff',
    'is_active',
  )
  fieldsets = (
    (None, {
      'fields': (
        'username',
        'email',
      )
    }),
    ('Personal info', {
      'fields':
      ('first_name', 'phone_number', 'last_name', 'date_of_birth', 'location')
    }),
    ('Permissions', {
      'fields':
      ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
    }),
  )
  add_fieldsets = ((None, {
    'classes': ('wide', ),
    'fields': ('username', 'email', 'password1', 'password2', 'location',
               'date_of_birth', 'is_staff', 'is_active')
  }), )


admin.site.register(BaseUser, BaseUserAdmin)
