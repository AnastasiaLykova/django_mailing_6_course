from django.contrib import admin

from mailing.models import Mailing, Message, Logs


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('datetime','status','creator',)
    list_filter = ('datetime',)
    search_fields = ('datetime',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('heading','content','pk', 'mailing',)
    list_filter = ('heading',)
    search_fields = ('heading',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('datetime','change_time','status', 'response',)
    list_filter = ('datetime',)
    search_fields = ('datetime',)

