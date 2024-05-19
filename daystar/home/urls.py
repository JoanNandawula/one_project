# from django urls.import path

from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dash/', views.dash, name='dash'),#dashboard
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),#login
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),#logout



    path('bdeparture/', views.bdeparture, name='bdeparture'),#babydeparture
    path('bdeparturelist/',views.bdeparturelist, name='bdeparturelist'),#babydeparturelist
    path('bpayment/',views.bpayment, name='bpayment'),#babypayment
    
   

    path('doll/',views.doll,name='doll'),#doll
    path('dollscorner/<int:dolls_id>/', views.dollscorner, name='dollscorner'),#dollcorner
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),#add_to_stoack
    path('all_sales/',views.all_sales,name='all_sales'),# all sales
    path('issue_item/<str:pk>',views.issue_item,name='issue_item'),#issue items
    path('shopform/',views.shopform,name='shopform'),
    path('shopstock/',views.shopstock, name='shopstock'),
    path('receipt/',views.receipt,name='receipt'),#receipt
    path('receipt_detail/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),#receipt details

    #sitterregistration
    path('sittersform/', views.sittersform, name='sittersform'),
    path('sitterslist/',views.sitterslist, name='sitterslist'),
    path('sitterview/<int:id>/',views.sitterview,name='sitterview'),
    path('spayment/',views.spayment, name='spayment'),
    path('spaymentlist/',views.spaymentlist, name='spaymentlist'),
    path('bpaymentlist/',views.bpaymentlist, name='bpaymentlist'),
    path('sittersedit/<int:id>/', views.sittersedit, name='sittersedit'),
    path('sarrival/',views.sarrival, name='sarrival'),
    path('sarrivallist/',views.sarrivallist, name='sarrivallist'),

    #babyregistration
    path('babesform/', views.babesform, name='babesform'),
    path('babyslist/',views.babyslist, name='babyslist'),
    path('babyview/<int:id>/',views.babyview,name='babyview'),
    path('babyedit/<int:id>/',views.babyedit,name='babyedit'),
]
