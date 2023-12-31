# Generated by Django 4.2.5 on 2023-09-20 15:19

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('Male', 'male'), ('Female', 'Female')], max_length=10)),
                ('telephone', models.PositiveIntegerField()),
                ('date_of_birth', models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date.today)])),
                ('home_address', models.CharField(max_length=300)),
                ('Registered_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OtherIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=300)),
                ('amount', models.PositiveIntegerField()),
                ('date_of_income', models.DateTimeField()),
                ('receipt', models.ImageField(blank=True, upload_to='income/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=300)),
                ('amount', models.PositiveIntegerField()),
                ('date_of_expense', models.DateTimeField()),
                ('receipt', models.ImageField(blank=True, upload_to='deposits/%Y/%m/%d')),
                ('user_responsible', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='twaaku_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_used', models.PositiveIntegerField()),
                ('amount_cash', models.PositiveIntegerField()),
                ('total_amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('year', models.PositiveIntegerField()),
                ('deposited_by', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='pending', max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twaaku_app.employee')),
            ],
        ),
    ]
