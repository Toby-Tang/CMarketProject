"""CMarketProject URL Configuration"""

from django.conf.urls import url
from django.contrib import admin
from CMarket import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^post/', views.post, name='post'),
    url(r'^public/', views.public, name='public'),
    url(r'^private/', views.private, name='private'),
]
