from django.urls import path
from . import views

app_name='blog_app'

urlpatterns=[
    path('', views.IndexView, name='index'),
    
]
