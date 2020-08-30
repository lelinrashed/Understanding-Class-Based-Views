"""cbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from dashboard.views import DashboardTemplateView, MyView, BookDetail, BookListView, BookCreateView, BookUpdateView, \
    BookDeleteView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('someview/', MyView.as_view(), name='home'),
    path('about/', DashboardTemplateView.as_view(), name='about'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<slug:slug>/', BookDetail.as_view(), name='book_detail'),
    path('book/<slug:slug>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book/<slug:slug>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('admin/', admin.site.urls),
]
