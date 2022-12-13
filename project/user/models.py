from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import UserManager, PermissionsMixin
#


class User(AbstractBaseUser, PermissionsMixin):
  avatar = models.ImageField('Profile Photo', upload_to='user_avatar/', null=True, blank=True)
  first_name = models.CharField('Name', max_length=255, null=True, blank=True)
  last_name = models.CharField('Surname', max_length=255, null=True, blank=True)
  email = models.EmailField('email', unique=False, null=True, blank=True)
  username = models.CharField('username', max_length=255, unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)  # a superuser
  last_login = models.DateTimeField(null=True, blank=True)
  date_joined = models.DateTimeField(default = timezone.now)
  phone_number = models.CharField('Phone', max_length=13, unique=True)
  # sms_code = models.CharField('СМС код', default='', max_length=9)
  # temp = models.CharField('Temprorary', default='', max_length=200)
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = []
  objects = UserManager()

  def __str__(self):
    return self.username

  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'



class RegisterUser(AbstractBaseUser):
  username = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  password1 = models.CharField(max_length=100)
  password2 = models.CharField(max_length=100)


class LoginUser(AbstractBaseUser):
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
