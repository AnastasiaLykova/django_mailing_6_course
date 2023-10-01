from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDeleteView, MailingDetailView, create_mailing

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing'),
    path('article/<int:pk>/', MailingDetailView.as_view(), name='detail_mailing'),
    path('create/', create_mailing, name='create_mailing'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
]