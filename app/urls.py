from django.urls import path
from . import views

urlpatterns = [
  path('', views.user, name='user'),
  path('create', views.create_user, name='create_user')
]
