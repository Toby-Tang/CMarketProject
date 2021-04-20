"""CMarketProject URL Configuration"""

from django.conf.urls import url
from django.contrib import admin
from CMarket import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
]
