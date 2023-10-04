import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class DepositFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte')
    end_date = DateFilter(field_name="date", lookup_expr='lte')
    # amount = CharFilter(field_name="amount", lookup_expr='icontains')


    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = [ 'date_created','receipt','deposited_by','amount_used','amount_cash','total_amount','date','year']



class ExpenseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_of_expense", lookup_expr='gte')
    end_date = DateFilter(field_name="date_of_expense", lookup_expr='lte')
    # amount = CharFilter(field_name="amount", lookup_expr='icontains')


    class Meta:
        model = Expense
        fields = '__all__'
        exclude = [ 'person_responsible', 'date_of_expense','receipt','amount']

class PurchaseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_of_expense", lookup_expr='gte')
    end_date = DateFilter(field_name="date_of_expense", lookup_expr='lte')
    # amount = CharFilter(field_name="amount", lookup_expr='icontains')


    class Meta:
        model = Expense
        fields = '__all__'
        exclude = [ 'person_responsible', 'date_of_expense','receipt','amount']
