from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Employee,Deposit,Expense,OtherIncome, Purchase
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import EmployeeForm,DepositForm,OtherIncomeForm, ExpenseForm,PurchaseForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q
from django.db.models import Sum, Avg, Count

from .filters import DepositFilter,ExpenseFilter
from django.db import connection
from django.db.models.expressions import RawSQL
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import csv



@login_required(login_url='login')
def home(request):
    total_employees = Employee.objects.all().count() #aggregate(Count('member_id'))
    pending_deposits = Deposit.objects.filter(status='pending').count()
    approved_deposits = Deposit.objects.filter(status='Approved').count()
    deposits = Deposit.objects.all().order_by("-date_created") 
    myFilter = DepositFilter(request.GET, queryset=deposits)
    deposits = myFilter.qs
    expenses_total = Expense.objects.all().aggregate(models.Sum('amount'))['amount__sum'] or 0 
    savings_total = Deposit.objects.filter(status='approved').aggregate(models.Sum('total_amount'))['total_amount__sum'] or 0 
    # savings_total = Deposit.objects.filter(status='approved').aggregate(models.Sum('amount_cash'))['amount_cash__sum'] or 0 
    # savings_total = Deposit.objects.filter(status='approved').aggregate(models.Sum('amount_cash'))['amount_cash__sum'] or 0 
    otherincome = OtherIncome.objects.aggregate(models.Sum('amount'))['amount__sum'] or 0

    current_balance = savings_total + otherincome - expenses_total 

    grand_total = savings_total + expenses_total + otherincome

    context = {
        'pending_deposits': pending_deposits,
        'approved_deposits': approved_deposits,
        'total_employees': total_employees, 
        # 'total_savings': total_savings,
        'deposits': deposits,
        'myFilter': myFilter, 
        'current_balance': current_balance,
        'savings_total': savings_total,
        'expenses_total':expenses_total,
        'grand_total': grand_total,
        
        'otherincome':otherincome,
        
      }

    return render(request,'dashboard.html', context)
    

def index(request):
    context = {
        'variable1': 'Hello',
        'variable2': 'World',
    }
    return render(request, 'index.html', context)


def employee(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    deposits = employee.deposit_set.all().order_by('-date_created')
    expenses = employee.expense_set.all().order_by('-date_of_expense')
    purchases = employee.purchase_set.all().order_by('-date_of_purchase')
    used_total = employee.deposit_set.filter(status='Approved').aggregate(models.Sum('amount_used'))['amount_used__sum'] or 0
    cash_total = employee.deposit_set.filter(status='Approved').aggregate(models.Sum('amount_cash'))['amount_cash__sum'] or 0
    # ind_fine = member.fine_set.filter(status='unpaid').aggregate(models.Sum('amount'))['amount__sum'] or 0
    # myFilter = DepositFilter(request.GET, queryset=deposits)
    # deposits = myFilter.qs
    
    context = {
                'employee': employee, 
                'deposits': deposits, 
                'purchases':purchases,
                'expenses':expenses,
                'used_total':used_total,
                # 'myFilter': myFilter,
                'cash_total': cash_total,
    }

    return render(request, 'emp_report.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else: 
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def createEmployee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}
    return render(request, 'employee_form.html', context)

def updateEmployee(request, emp_id):

    employee = Employee.objects.get(emp_id=emp_id)
    form = EmployeeForm(instance=employee)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'employee_form.html', context) 
    

def deleteEmployee(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    if request.method == "POST":
        employee.delete()
        return redirect('home')

    context = {'item': employee } 

    return render(request, 'delete_employee.html', context) 

def allEmployee(request):

    employee_list = Employee.objects.all()  
         

    context = {
                'employee_list': employee_list, 
                    
        }  

    return render(request, 'all_employee.html', context )


def create_deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DepositForm()
    return render(request, 'create_deposit.html', {'form': form})


def updateDeposit(request, id):
    deposit = Deposit.objects.get(id=id)
    form = DepositForm(instance=deposit)

    if request.method == "POST":
        form = DepositForm(request.POST, instance=deposit)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form } 

    return render(request, 'deposit_create.html', context)         

def deleteDeposit(request, id):
    deposit = Deposit.objects.get(id=id)
    if request.method == "POST":
        deposit.delete()
        return redirect('/')

    context = {'item': deposit } 

    return render(request, 'delete_deposit.html', context)

def allDeposit(request):
    search_deposit = request.GET.get('search')
    if search_deposit:

        deposits = Deposit.objects.filter(Q(amount__icontains=search_deposit) |
                             Q(purpose__icontains=search_deposit) |
                             Q(date_created__icontains=search_deposit))
    else:
        # If not searched, return default members
        sales = Deposit.objects.all().order_by("-date") 
        myFilter = DepositFilter(request.GET, queryset=sales)
        sales = myFilter.qs   
         
        context = {'sales': sales,
                    'myFilter': myFilter
        } #'members': members} 

    return render(request, 'all_deposits.html', context )

def createOtherIncome(request):
    if request.method == 'POST':
        form = OtherIncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_otherincome')
    else:
        form = OtherIncomeForm()
    return render(request, 'create_otherincome.html', {'form': form})


def updateOtherIncome(request, id):
    asset = OtherIncome.objects.get(id=id)
    form = OtherIncomeForm(instance=asset)

    if request.method == "POST":
        form = OtherIncomeForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('all_otherincome')

    context = {'form': form } 

    return render(request, 'create_otherincome.html', context)         

def deleteOtherIncome(request, id):
    asset = OtherIncome.objects.get(id=id)
    if request.method == "POST":
        asset.delete()
        return redirect('all_otherincome')

    context = {'asset': asset } 

    return render(request, 'delete_otherincome.html', context)   

def allOtherIncome(request):

    otherincome_list = OtherIncome.objects.all().order_by("-date_of_income")   
         

    context = {
                'otherincome_list': otherincome_list, 
                    
        }  

    return render(request, 'all_otherincome.html', context )


def createExpense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ExpenseForm()
    return render(request, 'create_expense.html', {'form': form})


def updateExpense(request, id):
    expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=expense)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form } 

    return render(request, 'create_expense.html', context)         

def deleteExpense(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        expense.delete()
        return redirect('home')

    context = {'expense': expense } 

    return render(request, 'delete_expense.html', context) 

def allExpense(request):
    search_expense = request.GET.get('search')
    if search_expense:
        expenses = Expense.objects.filter(
                             Q(purpose__icontains=search_expense) |
                             Q(date_created__icontains=search_expense))
    else:
        # If not searched, return default members
        expenses = Expense.objects.all().order_by("-date_of_expense") 
        myFilter = ExpenseFilter(request.GET, queryset=expenses)
        expenses = myFilter.qs   
         
        context = {
                    'expenses': expenses,
                    'myFilter': myFilter
                    }
    return render(request, 'all_expenses.html', context )


def createPurchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PurchaseForm()
    return render(request, 'create_purchase.html', {'form': form})


def updatePurchase(request, id):
    purchase = Expense.objects.get(id=id)
    form = PurchaseForm(instance=purchase)

    if request.method == "POST":
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form } 

    return render(request, 'create_purchase.html', context)         

def deletePurchase(request, id):
    purchase = Purchase.objects.get(id=id)
    if request.method == "POST":
        purchase.delete()
        return redirect('/')

    context = {'purchase': purchase } 

    return render(request, 'delete_purchase.html', context)   

def allPurchase(request):

    purchase_list = Purchase.objects.all()  
         

    context = {
                'purchase_list': purchase_list, 
                    
        }  

    return render(request, 'all_purchases.html', context )