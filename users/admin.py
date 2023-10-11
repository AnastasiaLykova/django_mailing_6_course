from django.contrib import admin

from users.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'verify_key', 'is_verified',)
    list_filter = ('email',)
    search_fields = ('email',)