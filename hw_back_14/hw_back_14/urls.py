"""
URL configuration for hw_back_14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
import debug_toolbar
from news.views import sign_up
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from news.views import NewsCreatingView, NewsDetailsView, NewsDeletingView, NewsListingView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path("news/", include("news.urls")),
    path('auth/', include('django.contrib.auth.urls')), 
    path('auth/sign_up/', sign_up, name='sign_up'),
    path('auth/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("api/news/add/", NewsCreatingView.as_view(), name="news_create"),
    path("api/news/<int:pk>/", NewsDetailsView.as_view(), name="news_detail"),
    path("api/news/<int:pk>/delete/", NewsDeletingView.as_view(), name="news_delete"),
    path("api/news/", NewsListingView.as_view(), name="news_list")
]
