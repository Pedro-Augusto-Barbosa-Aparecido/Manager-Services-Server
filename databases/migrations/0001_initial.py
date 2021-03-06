# Generated by Django 3.2.9 on 2021-11-06 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutsourcingDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outsourcing_type', models.CharField(choices=[('l', 'By level'), ('t', 'By item')], max_length=1)),
                ('outsourcing_id', models.CharField(max_length=10, verbose_name='Non-Employee ID')),
                ('legacy_sm', models.CharField(max_length=8, verbose_name='Legacy SRN')),
                ('status', models.CharField(choices=[('e', 'Active'), ('op', 'Open'), ('ol', 'On leave'), ('r', 'Inactive'), ('c', 'Canceled'), ('h', 'Hold')], max_length=2)),
                ('tl_id', models.CharField(max_length=10, verbose_name='TL ID')),
                ('tl_name', models.CharField(max_length=40, verbose_name='TL Name')),
                ('is_tl', models.BooleanField(default=False, verbose_name='Is Team Leader')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('actual_release_date', models.DateField(blank=True, null=True, verbose_name='Release date')),
                ('planned_start_date', models.DateField(blank=True, null=True, verbose_name='Planned start date')),
                ('planned_release_date', models.DateField(blank=True, null=True, verbose_name='Planned release date')),
                ('laptop', models.PositiveSmallIntegerField(default=0)),
                ('epi', models.PositiveSmallIntegerField(default=0, verbose_name='EPI')),
                ('smartphone', models.PositiveSmallIntegerField(default=0)),
                ('car', models.PositiveSmallIntegerField(default=0)),
                ('other', models.CharField(blank=True, max_length=255, null=True)),
                ('huawei_responsible_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Service Responsible')),
                ('huawei_responsible_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Service Responsible ID')),
                ('huawei_responsible_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Service Responsible email')),
                ('remarks', models.CharField(max_length=80)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.account')),
                ('branch_office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.branchoffice')),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.businessunit')),
                ('cost_owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.costowner')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.department')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.project')),
                ('service_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.servicelevel')),
                ('service_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.servicelocation')),
                ('service_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.servicename')),
                ('service_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.servicetype')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.supplier')),
            ],
            options={
                'verbose_name': 'Outsourcing',
                'verbose_name_plural': 'Outsourcing',
                'ordering': ('legacy_sm', 'outsourcing_id'),
            },
        ),
        migrations.CreateModel(
            name='InternDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intern_id', models.CharField(max_length=80, unique=True, verbose_name='Huawei ID')),
                ('intern_name', models.CharField(max_length=80, verbose_name='Name')),
                ('intern_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('status', models.CharField(choices=[('o', 'Active'), ('r', 'Replacing'), ('l', 'Inactive')], default='o', max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('supervisor_id', models.CharField(blank=True, max_length=80, null=True)),
                ('supervisor_name', models.CharField(blank=True, max_length=80, null=True)),
                ('contract_start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('planned_contract_start_date', models.DateField(blank=True, null=True, verbose_name='Planned start date')),
                ('contract_end_date', models.DateField(blank=True, null=True, verbose_name='Contract end date')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release date')),
                ('planned_release_date', models.DateField(blank=True, null=True, verbose_name='Planned release date')),
                ('comments', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.account')),
                ('base_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.servicelocation')),
                ('branch_office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.branchoffice')),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.businessunit')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.department')),
                ('detail_business_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.detailbusinessunit')),
                ('job_role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.jobrole')),
                ('sub_business_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.subbusinessunit')),
            ],
            options={
                'verbose_name': 'Intern',
                'verbose_name_plural': 'Intern',
                'ordering': ('intern_id', 'intern_name'),
            },
        ),
        migrations.CreateModel(
            name='HuaweiDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=80, unique=True, verbose_name='Huawei ID')),
                ('employee_name', models.CharField(max_length=80, verbose_name='Name')),
                ('employee_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release date')),
                ('planned_start_date', models.DateField(blank=True, null=True, verbose_name='Planned start date')),
                ('planned_release_date', models.DateField(blank=True, null=True, verbose_name='Planned release date')),
                ('status', models.CharField(choices=[('a', 'Active'), ('i', 'Inactive'), ('c', 'Canceled')], default='a', max_length=1)),
                ('nationality', models.CharField(choices=[('local', 'China'), ('chn', 'Local')], max_length=5)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('comments', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.account')),
                ('base_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.servicelocation')),
                ('branch_office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.branchoffice')),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.businessunit')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.department')),
                ('detail_business_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.detailbusinessunit')),
                ('job_role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.jobrole')),
                ('sub_business_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.subbusinessunit')),
            ],
            options={
                'verbose_name': 'Self Owned',
                'verbose_name_plural': 'Self Owned',
                'ordering': ('employee_id', 'employee_name'),
            },
        ),
    ]
