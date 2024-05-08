# from django urls.import path

from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dash/', views.dash, name='dash'),#dashboard
    path('bdeparture/', views.bdeparture, name='bdeparture'),#babydeparture
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),#login
    path('arrivallist/',views.arrivallist, name='arrivallist'),# babyarrivall
    path('sarrivallist/',views.sarrivallist, name='sarrivallist'),#sitterarrivallist
    path('bdeparturelist/',views.bdeparturelist, name='bdeparturelist'),#babydeparturelist
    path('bpayment/',views.bpayment, name='bpayment'),#babypayment
    path('sitterpayment/',views.Sitterpayment, name='sitterpayment'),#sitterpayment
    path('arrival/',views.arrival, name='arrival'),#babyarrival
    path('sarrival/',views.sarrival, name='sarrival'),#sitterarrival
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),#logout

    path('doll/',views.doll,name='doll'),#doll
    path('dollscorner/<int:dolls_id>/', views.dollscorner, name='dollscorner'),#dollcorner
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),#add_to_stoack
    path('all_sales/',views.all_sales,name='all_sales'),# all sales
    path('issue_item/<str:pk>',views.issue_item,name='issue_item'),#issue items
    path('receipt/',views.receipt,name='receipt'),#receipt
    path('receipt_detail/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),#receipt details
    #sitterregistration
    path('sittersform/', views.sittersform, name='sittersform'),
    path('sitterslist/',views.sitterslist, name='sitterslist'),
    path('sitterview/<int:id>/',views.sitterview,name='sitterview'),
    # path('sittersedit/<int:id>/', views.sittersedit, name='sittersedit'),
    # path('sittersdelete/<int:id>/', views.sittersdelete, name='sittersdelete'),
    #babyregistration
    path('babesform/', views.babesform, name='babesform'),
    path('babyslist/',views.babyslist, name='babyslist'),
    path('babyview/<int:id>/',views.babyview,name='babyview'),
    path('babyedit/<int:id>/',views.babyedit,name='babyedit'),
]
