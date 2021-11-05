import abc
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.enums import ChoicesMeta

# Create your models here.

class Permission(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class User(AbstractBaseUser, BaseUserManager):
    
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    full_name = ""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, blank=False, null=False)

    last_login = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    permissions = models.ManyToManyField(Permission, blank=True, null=False)

    active = models.BooleanField(default=True)

    is_employee = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    object = BaseUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

        ordering = ("first_name", "last_name")

    def __str__(self) -> str:
        return self.full_name

    def save(self, *args, **kwargs) -> None:
        self.full_name = f"{self.first_name}{self.last_name}"

        return super().save(*args, **kwargs, full_name=self.full_name)

    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"
