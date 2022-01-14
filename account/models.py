from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string


class UserManager (BaseUserManager):
    def _create (self, email, password, **extra_fields):
        if not email:
            raise VallueError('емайл не может быть пустым')
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user (self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField (primary_key=True)
    name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects=UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff
    def has_perm (self, perm, obj=None):
        return self.is_staff

    def create_activasion_code(self):
        code = get_random_string(10)
        self.create_activasion_code=code
        self.save()
