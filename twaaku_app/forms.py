from django.contrib.auth.models import User
from django import forms
from .models import Employee,Deposit,Expense,OtherIncome,Purchase
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from bootstrap_datepicker_plus.widgets import DatePickerInput


class EmployeeForm(ModelForm):
    date_of_birth= forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'}))
    class Meta:
        model = Employee
        fields = '__all__'

class DepositForm(ModelForm):
    date= forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'}))
    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = ["status"]


class ExpenseForm(ModelForm):
    date_of_expense = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Expense
        fields = '__all__'

class PurchaseForm(ModelForm):
    date_of_purchase = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Purchase
        fields = '__all__'

class OtherIncomeForm(ModelForm):
    date_of_income = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = OtherIncome
        fields = '__all__'

