from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientsListView, ClientsDetailView, ClientsCreateView, ClientsUpdateView, ClientsDeleteView

app_name = ClientsConfig.name

urlpatterns = [
    path('', ClientsListView.as_view(), name='clients_list'),
    path('clients/<int:pk>/', ClientsDetailView.as_view(), name='detail_client'),
    path('create/', ClientsCreateView.as_view(), name='create_client'),
    path('update/<int:pk>/', ClientsUpdateView.as_view(), name='update_client'),
    path('delete/<int:pk>/', ClientsDeleteView.as_view(), name='delete_client'),
]
