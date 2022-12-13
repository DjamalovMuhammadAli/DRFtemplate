from django.contrib import admin

from user.models import User, RegisterUser, LoginUser

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
  fieldsets = (
    (None, {'fields': ('email', 'password', 'username', 'first_name', 'last_name', 'phone_number')}),
    ('Permissions', {'fields': (
      'is_active', 
      'is_staff', 
      'is_superuser',
      'groups', 
      'user_permissions',
    )}),
  )
  add_fieldsets = (
    (
      None,
      {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2')
      }
    ),
  )

  list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
  list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
  search_fields = ('email',)
  ordering = ('email',)
  filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)


admin.site.register(User)




admin.site.register(RegisterUser)
admin.site.register(LoginUser)
