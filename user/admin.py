from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_superuser', 'is_staff')
    search_fields = ['username']


admin.site.register(User, UserAdmin)
