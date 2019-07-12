from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
  path('',views.index, name='index'), #this url goto posts/index or post/ post index view
]
