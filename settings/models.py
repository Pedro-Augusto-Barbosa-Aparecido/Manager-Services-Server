from django.db import models
from django.db.models.manager import Manager

from users.models import User

# Create your models here.

class BaseModel(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ""
        verbose_name_plural = ""

        ordering = ()

class Account(BaseModel):
   
    name = models.CharField(max_length=30, blank=False, null=False)
    manager = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)

    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class Department(BaseModel):

    name = models.CharField(max_length=30, blank=False, null=False)
    approver = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    active = models.BooleanField(default=True)
    use_bu_on_dashboard = models.BooleanField(default=False)


class ResourceDepartment(BaseModel):
    
    name = models.CharField(max_length=30, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Resource Department"
        verbose_name_plural = "Resource Departments"

        ordering = ("name")
