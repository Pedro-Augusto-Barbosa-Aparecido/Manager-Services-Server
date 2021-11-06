from django.db import models

from settings.models import Account, BranchOffice, BusinessUnit, CostOwner, Department, DetailBusinessUnit, JobRole, Project, ServiceLevel, ServiceLocation, ServiceName, ServiceType, SubBusinessUnit, Supplier

class OutsourcingDatabase(models.Model):
    STATUS_ENTERED = "e"
    STATUS_OPEN = "op"
    STATUS_ON_LEAVE = "ol"
    STATUS_RELEASED = "r"
    STATUS_CANCELED = "c"
    STATUS_HOLD = "h"
    STATUS_CHOICES = (
        (STATUS_ENTERED, "Active"),
        (STATUS_OPEN, "Open"),
        (STATUS_ON_LEAVE, "On leave"),
        (STATUS_RELEASED, "Inactive"),
        (STATUS_CANCELED, "Canceled"),
        (STATUS_HOLD, "Hold"),
    )

    OUT_BY_LEVEL = "l"
    OUT_BY_ITEM = "t"

    CHOICES_OUT = (
        (OUT_BY_LEVEL, "By level"),
        (OUT_BY_ITEM, "By item"),
    )

    outsourcing_type = models.CharField(max_length=1, blank=False, null=False, choices=CHOICES_OUT)
    outsourcing_id = models.CharField(max_length=10, blank=False, null=False, verbose_name="Non-Employee ID")

    legacy_sm = models.CharField(max_length=8, blank=False, null=False, verbose_name="Legacy SRN")

    status = models.CharField(max_length=2, blank=False, null=False, choices=STATUS_CHOICES)

    tl_id = models.CharField(max_length=10, blank=False, null=False, verbose_name="TL ID")
    tl_name = models.CharField(max_length=40, blank=False, null=False, verbose_name="TL Name")
    is_tl = models.BooleanField(default=False, verbose_name="Is Team Leader")

    account = models.ForeignKey(Account, blank=False, null=False, on_delete=models.PROTECT)
    business_unit = models.ForeignKey(BusinessUnit, blank=False, null=False, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, blank=False, null=False, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.PROTECT)
    cost_owner = models.ForeignKey(CostOwner, blank=False, null=False, on_delete=models.PROTECT)
    branch_office = models.ForeignKey(BranchOffice, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.PROTECT, null=True, blank=True)
    service_name = models.ForeignKey(ServiceName, on_delete=models.PROTECT, null=True, blank=True)
    service_level = models.ForeignKey(ServiceLevel, on_delete=models.PROTECT, null=True, blank=True)
    service_location = models.ForeignKey(ServiceLocation, on_delete=models.PROTECT, null=True, blank=True)

    start_date = models.DateField(verbose_name="Start date", blank=True, null=True)
    actual_release_date = models.DateField(verbose_name="Release date", null=True, blank=True)
    planned_start_date = models.DateField(verbose_name="Planned start date", null=True, blank=True)
    planned_release_date = models.DateField(verbose_name="Planned release date", blank=True, null=True)

    laptop = models.PositiveSmallIntegerField(default=0)
    epi = models.PositiveSmallIntegerField(default=0, verbose_name="EPI")
    smartphone = models.PositiveSmallIntegerField(default=0)
    car = models.PositiveSmallIntegerField(default=0)
    other = models.CharField(max_length=255, blank=True, null=True)

    huawei_responsible_name = models.CharField(max_length=255, verbose_name="Service Responsible", null=True, blank=True)
    huawei_responsible_id = models.CharField(max_length=255, verbose_name="Service Responsible ID", null=True, blank=True)
    huawei_responsible_email = models.EmailField(verbose_name="Service Responsible email", null=True, blank=True)


    remarks = models.CharField(max_length=80, blank=False, null=False)

    class Meta:
        verbose_name = "Outsourcing"
        verbose_name_plural = "Outsourcing"

        ordering = ("legacy_sm", "outsourcing_id")

    def __str__(self) -> str:
        return f"Non-Employee ID: {self.outsourcing_id}"

class HuaweiDatabase(models.Model):
    STATUS_ACTIVE = "a"
    STATUS_INACTIVE = "i"
    STATUS_CANCELED = 'c'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
        (STATUS_CANCELED, 'Canceled'),
    )

    GENDER_FEMALE = "F"
    GENDER_MALE = "M"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    ORIGIN_CHN = "chn"
    ORIGIN_LOCAL = "local"

    ORIGIN_CHOICES = (
        (ORIGIN_LOCAL, "China"),
        (ORIGIN_CHN, "Local"),
    )

    employee_id = models.CharField(max_length=80, unique=True, verbose_name="Huawei ID")
    employee_name = models.CharField(max_length=80, verbose_name="Name")

    employee_email = models.EmailField(null=True, blank=True, verbose_name="Email")

    start_date = models.DateField(verbose_name="Start date", null=True, blank=True) 
    release_date = models.DateField(verbose_name="Release date", null=True, blank=True)
    planned_start_date = models.DateField(verbose_name="Planned start date", null=True, blank=True)
    planned_release_date = models.DateField(verbose_name="Planned release date", null=True, blank=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    nationality = models.CharField(max_length=5, choices=ORIGIN_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    base_location = models.ForeignKey(ServiceLocation, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.PROTECT)
    sub_business_unit = models.ForeignKey(SubBusinessUnit, on_delete=models.PROTECT, null=True, blank=True)
    detail_business_unit = models.ForeignKey(DetailBusinessUnit, on_delete=models.PROTECT, null=True, blank=True)
    branch_office = models.ForeignKey(BranchOffice, on_delete=models.PROTECT, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, blank=True)
    job_role = models.ForeignKey(JobRole, on_delete=models.PROTECT)

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Self Owned"
        verbose_name_plural = "Self Owned"

        ordering = ("employee_id", "employee_name")

    def __str__(self) -> str:
        return self.employee_name

class InternDatabase(models.Model):
    STATUS_ON_DUTY = "o"
    STATUS_REPLACING = "r"
    STATUS_LEFT = "l"
    STATUS_CHOICES = (
        (STATUS_ON_DUTY, "Active"),
        (STATUS_REPLACING, "Replacing"),
        (STATUS_LEFT, "Inactive"),
    )

    GENDER_FEMALE = "F"
    GENDER_MALE = "M"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    intern_id = models.CharField(max_length=80, unique=True, verbose_name="Huawei ID")
    intern_name = models.CharField(max_length=80, verbose_name="Name")

    intern_email = models.EmailField(null=True, blank=True, verbose_name="Email")

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_ON_DUTY)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    base_location = models.ForeignKey(ServiceLocation, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.PROTECT)
    sub_business_unit = models.ForeignKey(SubBusinessUnit, on_delete=models.PROTECT, null=True, blank=True)
    detail_business_unit = models.ForeignKey(DetailBusinessUnit, on_delete=models.PROTECT, null=True, blank=True)
    branch_office = models.ForeignKey(BranchOffice, on_delete=models.PROTECT, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, blank=True)
    job_role = models.ForeignKey(JobRole, on_delete=models.PROTECT, null=True, blank=True)

    supervisor_id = models.CharField(max_length=80, null=True, blank=True)
    supervisor_name = models.CharField(max_length=80, null=True, blank=True)

    contract_start_date = models.DateField(verbose_name="Start date", null=True, blank=True) 
    planned_contract_start_date = models.DateField(verbose_name="Planned start date", null=True, blank=True) 
    contract_end_date = models.DateField(verbose_name="Contract end date", null=True, blank=True)
    release_date = models.DateField(verbose_name="Release date", null=True, blank=True)
    planned_release_date = models.DateField(verbose_name="Planned release date", null=True, blank=True)  

    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Intern"
        verbose_name_plural = "Intern"

        ordering = ("intern_id", "intern_name")

    def __str__(self) -> str:
        return self.intern_name
