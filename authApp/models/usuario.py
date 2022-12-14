from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

from .Empresa  import Empresa

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
        username=username,
        password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    Username = models.CharField('Username', max_length = 30, unique=True)
    password = models.CharField('password', max_length = 256)
    Name = models.CharField('Name', max_length = 30)
    Email = models.EmailField('Email', max_length = 100,unique=True)
    Cedula = models.CharField('Cedula', max_length = 20, default=(0))
    Empresa = models.ForeignKey(Empresa, related_name='empresa_id', on_delete=models.CASCADE, default=(1))

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'Username'
