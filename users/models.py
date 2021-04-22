from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, name, tag, email, phone_number, password, **extra_fields):
        values = [name, tag, email]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError(f'The {field_name} value must be set')
        
        if not phone_number:
            raise ValueError('The given email must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, tag, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')

        return self._create_user(phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('name'), max_length=50)
    tag = models.CharField(_('tag'), max_length=32, unique=True)
    phone_number = models.CharField(_('phone number'), max_length=12)
    email = models.EmailField(_('email address'), max_length=64, unique=True)
    avatar = models.TextField(upload_to='media/avatars/', default='media/avatars/default_avatar.png')
    friend_list = models.ManyToManyField('self', symmetrical=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'tag', 'email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
