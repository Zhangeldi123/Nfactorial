from django.urls import path
from .views import NewsListView, NewsDetailView, AddNewsView, news_list_view, news_detail_view, add_news_view

urlpatterns = [
    path('', news_list_view, name='news_list'),
    path('<int:news_id>/', news_detail_view, name='news_detail'),
    path('add/', add_news_view, name='add_news'),
]

