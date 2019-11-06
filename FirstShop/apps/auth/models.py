from django.db import models
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class My_user(UserCreationForm):
    user = models.OneToOneField(UserCreationForm, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
