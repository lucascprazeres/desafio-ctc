from django.shortcuts import render

from app.models import User, Address

def home(request):
  users = User.objects.all().extra(
    select={
      'city': 'app_address.city',
      'neighborhood': 'app_address.neighborhood',
      'street': 'app_address.street',
      'house_number': 'app_address.house_number'
    },
    tables=['app_address'],
    where=['app_user.id=app_address.user_id']
  )

  context = {
    'users': users
  }

  return render(request, 'app/home.html', context)