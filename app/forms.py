from django import forms
from .models import User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    exclude = ()

    full_name: forms.TextInput(attrs={ 'autofocus': '' })
    mother_name: forms.TextInput()
    cpf: forms.TextInput()
    phone_number: forms.TextInput()
    city: forms.TextInput()
    neighborhood: forms.TextInput()
    street: forms.TextInput(attrs={ 'id': 'street' })
    house_number: forms.TextInput(attrs={ 'id': 'house_number' })