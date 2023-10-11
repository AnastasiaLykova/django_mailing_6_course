from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creation_date')
    list_filter = ('title',)
    search_fields = ('title',)