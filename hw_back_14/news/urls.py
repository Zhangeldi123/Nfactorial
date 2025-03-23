from django.urls import path
from .views import NewsListView, NewsDetailView, AddNewsView, news_list_view, news_detail_view, add_news_view
from .views import NewsUpdateView
from .views import delete_news_view, delete_comment_view

urlpatterns = [
    path('', news_list_view, name='news_list'),
    path('<int:news_id>/', news_detail_view, name='news_detail'),
    path('add/', add_news_view, name='add_news'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('<int:news_id>/delete/', delete_news_view, name='delete_news'),
    path('comment/<int:comment_id>/delete/', delete_comment_view, name='delete_comment')
]

