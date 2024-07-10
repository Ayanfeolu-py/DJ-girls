from django.urls import path 
from . import views


urlpatterns = [
    path('create', views.post_list, name='post-list')
]