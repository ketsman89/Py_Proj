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
from django.urls import path, include
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.HomePage.as_view(), name="home-page"),
    path('spravochniki/', include('spravochniki.urls', namespace='spravochniki')),  
    path('staff/', include('staff.urls', namespace='orders')),
    path('orders/', include('orders.urls', namespace='staff'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Этого не должно быть в продакшене, поэтому плючуем только в дев сервере,
# для этого пропишем условие:
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)