# Generated by Django 2.1.7 on 2019-09-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('emp_email', models.CharField(max_length=8, unique=True)),
                ('emp_address', models.CharField(max_length=250)),
                ('emp_city', models.CharField(max_length=50)),
                ('emp_created_at', models.DateTimeField(auto_now_add=True)),
                ('emp_updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]