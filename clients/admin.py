from django.contrib import admin

from clients.models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('email', 'fullname', 'annotation')
    list_filter = ('email',)
    search_fields = ('email', 'fullname')

