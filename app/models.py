from django.db import models

class User(models.Model):
  full_name = models.CharField(max_length=200)
  mother_name = models.CharField(max_length=200)
  cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
  phone_number = models.CharField(max_length=20, blank=True, null=True)
  city = models.CharField(max_length=50, blank=True, null=True)
  neighborhood = models.CharField(max_length=50, blank=True, null=True)
  street = models.CharField(max_length=50, blank=True, null=True)
  house_number = models.CharField(max_length=5, blank=True, null=True)