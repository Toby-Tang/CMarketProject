"""CMarketProject URL Configuration"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path
from django.views.generic import RedirectView

from CMarket import views

favicon_view = RedirectView.as_view(url='/static/CMarket/favicon.ico', permanent=True)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^post/', views.post, name='post'),
    url(r'^public/', views.public, name='public'),
    url(r'^private/', views.private, name='private'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^delete_posts/', views.delete_posts, name='delete_posts'),
    url(r'^delete_messages/', views.delete_messages, name='delete_messages'),
    re_path(r'^favicon\.ico$', favicon_view),
]

