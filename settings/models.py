from _typeshed import OpenBinaryModeReading
from django.db import models
from django.db.models.manager import Manager

from users.models import User


class Account(models.Model):
   
    name = models.CharField(max_length=30, blank=False, null=False)
    manager = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class Department(models.Model):

    name = models.CharField(max_length=30, blank=False, null=False)
    approver = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    active = models.BooleanField(default=True)
    use_bu_on_dashboard = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

        ordering = ("name")


class ResourceDepartment(models.Model):
    
    name = models.CharField(max_length=30, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Resource Department"
        verbose_name_plural = "Resource Departments"

        ordering = ("name")

class BusinessUnit(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    department = models.ForeignKey(Department, blank=False, null=False, on_delete=models.PROTECT)
    managers = models.ManyToManyField(User, blank=True, null=True)
    allowed_users = models.ManyToManyField(User, blank=True, null=True)

    active = models.BooleanField(default=True)
    available_for_request = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Business Unit"
        verbose_name_plural = "Business Units"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class SubBusinessUnit(models.Model):
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.PROTECT, blank=False, null=False)
    name = models.CharField(max_length=40, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sub Business Unit"
        verbose_name = "Sub Business Units"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class DetailBusinessUnit(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    sub_business_unit = models.ForeignKey(SubBusinessUnit, on_delete=models.PROTECT, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Detail Business Unit"
        verbose_name_plural = "Detail Business Units"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class ServiceType(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.PROTECT, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Service Type"
        verbose_name_plural = "Service Types"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name  

class ServiceName(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    service_type = models.ForeignKey(ServiceType, on_delete=models.PROTECT, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Service Name"
        verbose_name_plural = "Service Names"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class ServiceLevel(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    service_name = models.ForeignKey(ServiceType, on_delete=models.PROTECT, blank=False, null=False)
    sow = models.CharField(max_length=20, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Service Level"
        verbose_name_plural = "Service Levels"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class ServiceLocation(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False, unique=True)

    available_for_requests = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Service Location"
        verbose_name_plural = "Service Locations"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class BranchOffice(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False, unique=True)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Branch Office"
        verbose_name_plural = "Branch Offices"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class JobRole(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Job Role"
        verbose_name_plural = "Job Roles"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class CostOwner(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Cost Owner"
        verbose_name_plural = "Cost Owners"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class HPCPName(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "HPCP Name"
        verbose_name_plural = "HPCP Names"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    hpcp_name = models.ForeignKey(HPCPName, on_delete=models.PROTECT, blank=True, null=True)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    code = models.CharField(max_length=40, blank=False, null=False)

    account = models.ForeignKey(Account, blank=False, null=False, on_delete=models.PROTECT)

    active = models.BooleanField(default=True)

    class Meta: 
        verbose_name = "Project"
        verbose_name_plural = "Projects"

        ordering = ("name")

    def __str__(self) -> str:
        return self.name
