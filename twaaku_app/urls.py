from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
	 path("home/", views.home, name='home'),
 #    path('member_savings/', views.member_savings, name='member_savings'),
	# path('report/',views.report,name='report'),
	path("", views.index, name='index'),
	# path('member/<str:member_id>/', views.member, name='member'),
 #    path('relative/<int:id>/', views.relative, name='relative'),
	# path('signup/', views.signupPage, name="signup"),
	# path('register/', views.register, name='register'),
	 path('login/', views.loginPage, name="login"),
     path('logout/', views.logoutUser, name="logout"),
 #    path('user/', views.userPage, name="user-page"),
    
     path('create_employee/', views.createEmployee, name="create_employee"),
     path('update_employee/<str:emp_id>/', views.updateEmployee, name='update_employee'),
     path('delete_employee/<str:emp_id>/', views.deleteEmployee, name='delete_employee'),

     path('create_deposit/', views.create_deposit, name='create_deposit'),
     path('update_deposit/<int:id>/', views.updateDeposit, name='update_deposit'),
     path('delete_deposit/<int:id>/', views.deleteDeposit, name='delete_deposit'),

     path('create_expense/', views.createExpense, name='create_expense'),
     path('update_expense/<int:id>/', views.updateExpense, name='update_expense'),
     path('delete_expense/<int:id>/', views.deleteExpense, name='delete_expense'),

     path('create_purchase/', views.createPurchase, name='create_purchase'),
     path('update_purchase/<int:id>/', views.updatePurchase, name='update_purchase'),
     path('delete_purchase/<int:id>/', views.deletePurchase, name='delete_purchase'),

     path('create_otherincome/', views.createOtherIncome, name='create_otherincome'),
     path('update_otherincome/<int:id>/', views.updateOtherIncome, name='update_otherincome'),
     path('delete_otherincome/<int:id>/', views.deleteOtherIncome, name='delete_otherincome'),

     
     path('employee/<str:emp_id>/', views.employee, name='employee'),


 #    path('add_child_detail/', views.add_children_detail, name='add_child_detail'),
 #    path('add_relative_detail/', views.add_relative_detail, name='add_relative_detail'),
    path('all_deposit/', views.allDeposit, name='all_deposit'),
 #    path('all_fine/', views.allFines, name='all_fine'),
 #    path('fine/<int:fine_id>/', views.fine_detail, name='fine_detail'),
 #    path('fine/<int:fine_id>/make-payment/', views.make_payment, name='make_payment'),

 #    path('update_child/<int:id>/', views.updateChild, name='update_child'),
 #    path('update_relative/<int:id>/', views.updateRelative, name='update_relative'),

    path('all_expense/', views.allExpense, name='all_expense'),
    path('all_purchase/', views.allPurchase, name='all_purchase'),
    path('all_employee/', views.allEmployee, name='all_employee'),
 #    path('all_children/', views.allchildren, name='all_children'),
 #    path('all_relative/', views.allrelative, name='all_relative'),
    path('all_otherincome/', views.allOtherIncome, name='all_otherincome'),

 #    path('deposit_csv/', views.deposit_csv, name='deposit_csv'),
 #    path('relative_csv/', views.relative_csv, name='relative_csv'),
 #    path('member_txt/', views.member_txt, name='member_txt'),
    

]