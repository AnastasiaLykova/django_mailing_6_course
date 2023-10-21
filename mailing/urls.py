from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDeleteView, MailingDetailView, create_mailing, \
    MailingChangeStatusView, CreateMailingView, MessageListView, CreateMessageView, MessageDeleteView, LogsListView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing'),
    path('message', MessageListView.as_view(), name='message'),
    path('logs', LogsListView.as_view(), name='logs'),
    path('article/<int:pk>/', MailingDetailView.as_view(), name='detail_mailing'),
  #  path('create/', create_mailing, name='create_mailing'),
    path('create/', CreateMailingView.as_view(), name='create_mailing'),
    path('create_message/', CreateMessageView.as_view(), name='create_message'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),
    path('change/<int:pk>/', MailingChangeStatusView.as_view(), name='change_status'),
]
