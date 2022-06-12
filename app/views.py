from django.shortcuts import render, redirect

from app.models import User
from .forms import UserForm

def user(request):
  users = User.objects.all()

  context = {
    'users': users
  }

  return render(request, 'app/user.html', context)

def create_user(request):
  form = UserForm(request.POST or None)

  if request.POST:
    if form.is_valid():
      user = form.save(commit=False)
      print(user)
      user.save()
      return redirect('user')
    else:
      print('invalid')

  context = {
    'form': form
  }

  return render(request, 'app/create_user.html', context)