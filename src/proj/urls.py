"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from spravochniki import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('book-cbv/<int:pk>/', views.BookView.as_view(), name="view-book"),    
    path('book-delete-cbv/<int:pk>/', views.BookDeleteView.as_view(), name="delete-book"),
    path('book-list-cbv/', views.BookListView.as_view(), name="list-book"),   
    path('book-add-cbv/', views.BookCreateView.as_view(), name="add-book"),
    path('book-update-cbv/<int:pk>/', views.BookUpdateView.as_view(), name="update-book"),
    path('added/', views.succes_page, name="success-page"),
    path('send-email/', views.send_email, name="send-email"),
    path('', views.HomePage.as_view(), name="home-page"),

]
