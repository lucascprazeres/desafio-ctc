from django.urls import path
from . import views

urlpatterns = [
  path('', views.user, name='user'),
  path('create', views.create_user, name='create_user'),
  path('edit/<int:user_id>', views.edit_user, name='edit_user'),
  path('delete/<int:user_id>', views.delete_user, name='delete_user')
]
