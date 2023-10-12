from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, verify_key, UsersListView, UsersDetailView, UsersUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', verify_key, name='verify'),
    path('users_list/', UsersListView.as_view(), name='users_list'),
    path('clients/<int:pk>/', UsersDetailView.as_view(), name='detail_user'),
    path('update/<int:pk>/', UsersUpdateView.as_view(), name='update_user'),
]