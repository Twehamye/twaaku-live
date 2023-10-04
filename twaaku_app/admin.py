from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Expense)
#admin.site.register(OtherIncome)
# admin.site.register(Purchase)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ("emp_id","full_name","telephone","date_of_birth","home_address",)


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
	list_display = ('employee', 'amount_used','amount_cash','total_amount','date','deposited_by','status', 'date_created', )

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
	list_display = ("person_responsible","purpose","amount","date_of_expense","branch",)

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
	list_display = ("person_responsible","items","amount","date_of_purchase","branch",)

@admin.register(OtherIncome)
class OtherIncomeAdmin(admin.ModelAdmin):
	list_display = ("added_by","source","amount","date_of_income")