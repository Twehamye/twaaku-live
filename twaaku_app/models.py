from django.db import models
import datetime
from datetime import date  
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Employee(models.Model):
    sex_choices = (("Male","male"), ("Female","Female"))
    emp_id =models.CharField(max_length=10, primary_key=True )
    full_name = models.CharField(max_length=200, null=False)
    sex = models.CharField(max_length=10,choices = sex_choices)
    telephone = models.PositiveIntegerField()
    date_of_birth = models.DateField(validators=[MaxValueValidator(datetime.date.today)])
    parent_name = models.CharField(max_length=200, null=False)
    parent_telephone = models.PositiveIntegerField()
    home_address = models.CharField(max_length=300) 
    Registered_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):

        return self.emp_id + " " +self.full_name

class Deposit(models.Model):
    status_choices =(("pending","pending"),("Approved","Approved"),
                        ("Rejected","Rejected"))
    branch_choices =(("Nateete","Nateete"),("kisenyi","kisenyi"),
                    ("Kikajjo","Kikajjo"),("Other","Other"))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount_used = models.PositiveIntegerField()
    amount_cash = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    date = models.DateField()
    year = models.PositiveIntegerField()
    branch = models.CharField(max_length=200, null=False, choices = branch_choices)
    deposited_by = models.CharField(max_length=50,null=False)
    status = models.CharField(max_length=200, null=False, choices = status_choices, default="pending")
    date_created = models.DateTimeField(auto_now_add=True)

class Expense(models.Model):
    branch_choices =(("Nateete","Nateete"),("kisenyi","kisenyi"),
                    ("Kikajjo","Kikajjo"),("Other","Other"))
    purpose = models.CharField(max_length=300, null=False)
    amount = models.PositiveIntegerField()
    date_of_expense = models.DateField()
    branch = models.CharField(max_length=200, null=False, choices = branch_choices)
    person_responsible = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=None, null=False)
    receipt = models.ImageField(upload_to='deposits/%Y/%m/%d',blank=True)

    def __str__(self):
        return self.purpose +"  "+ str(self.amount)


class Purchase(models.Model):
    branch_choices =(("Nateete","Nateete"),("kisenyi","kisenyi"),
                    ("Kikajjo","Kikajjo"),("Other","Other"))
    items = models.CharField(max_length=300, null=False)
    amount = models.PositiveIntegerField()
    date_of_purchase = models.DateField()
    branch = models.CharField(max_length=30, null=False, choices = branch_choices)
    receipt_no = models.CharField(max_length=300)
    person_responsible = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT, default=None, null=False)
    receipt = models.ImageField(upload_to='deposits/%Y/%m/%d',blank=True)


class OtherIncome(models.Model):
    source = models.CharField(max_length=300, null=False)
    amount = models.PositiveIntegerField()
    date_of_income = models.DateField()
    added_by = models.CharField(max_length=50, null=False)
    receipt = models.ImageField(upload_to='income/%Y/%m/%d',blank=True)

