from django.contrib import admin

from django_boilerplate.user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'group', 'date_joined']
    ordering = ['date_joined']


admin.site.register(User, UserAdmin)
