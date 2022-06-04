# from django.conf.urls import url
from django.urls import re_path as url

from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
]