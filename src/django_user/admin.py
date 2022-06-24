from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User

# admin.site.register(User, UserAdmin)

fieldsets = list(AuthUserAdmin.fieldsets)


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    readonly_fields = ('email', 'failed_logins_count', 'failed_logins_started')
    fieldsets = fieldsets[:-1] + [('Important dates', {'fields': ('last_login', 'date_joined', 'failed_logins_count', 'failed_logins_started')})]
