from django.urls import path
from .views import NewsList, NewsDetail, NewsUpdate, NewsCreate, NewsDelete, Search


urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('search/', Search.as_view(), name='search'),
    path('<int:pk>', NewsDetail.as_view(), name='new_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
        ]
