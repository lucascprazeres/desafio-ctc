from django.shortcuts import render, redirect

from app.models import User
from .forms import UserForm

def user(request):
  users = User.objects.all()

  context = {
    'users': users
  }

  return render(request, 'app/user.html', context)

def search_user(request):
  if request.method == 'POST':
    searched_cpf = request.POST['searched']

    users = User.objects.filter(cpf__contains=searched_cpf)

    context = {
      'users': users
    }
    
    return render(request, 'app/user.html', context)
  
  return redirect('user')

def create_user(request):
  form = UserForm(request.POST or None)

  if request.POST:
    if form.is_valid():
      user = form.save(commit=False)
      user.save()
      return redirect('user')

  context = {
    'form': form
  }

  return render(request, 'app/create_user.html', context)

def edit_user(request, user_id):
  user = User.objects.get(pk=user_id)

  form = UserForm(request.POST or None, instance=user)

  if request.POST:
    if form.is_valid():
      user = form.save(commit=False)
      user.save()
      return redirect('user')

  context = {
    'form': form,
    'user_id': user_id
  }

  return render(request, 'app/edit_user.html', context)

def delete_user(request, user_id):
  user = User.objects.get(pk=user_id)
  user.delete()

  return redirect('user')