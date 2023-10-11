from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    GeneralView

app_name = BlogConfig.name

urlpatterns = [
    path('', GeneralView.as_view(), name='general'),
    path('article_list/', ArticleListView.as_view(), name='list'),
    path('article/<int:pk>/', cache_page(60)(ArticleDetailView.as_view()), name='article'),
    path('create/', ArticleCreateView.as_view(), name='create_article'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update_article'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete_article'),
]
