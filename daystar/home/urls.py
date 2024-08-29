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
    # path('home/', views.home, name='home'),



    path('bdeparture/', views.bdeparture, name='bdeparture'),#babydeparture
    path('bdeparturelist/',views.bdeparturelist, name='bdeparturelist'),#babydeparturelist
    path('bdepartureview/<int:id>/',views.bdepartureview,name='bdepartureview'),
    path('bdepartureedit/<int:id>/',views.bdepartureedit,name='bdepartureedit'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('bpaymentlist/',views.bpaymentlist, name='bpaymentlist'),
    
   

    path('doll/',views.doll,name='doll'),#doll
    path('dollscorner/<int:dolls_id>/', views.dollscorner, name='dollscorner'),#dollcorner
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),#add_to_stoack
    path('all_sales/',views.all_sales,name='all_sales'),# all sales
    path('issue_item/<str:pk>',views.issue_item,name='issue_item'),#issue items
    path('shopform/',views.shopform,name='shopform'),
    path('shopstock/',views.shopstock, name='shopstock'),
    path('receipt/',views.receipt,name='receipt'),#receipt
    path('receipt_detail/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),#receipt details
    path('shopstock/<int:id>/', views.shopstockview, name='shopstockview'),
    path('itemdelete/<int:id>/', views.itemdelete, name='itemdelete'),
    path('itemedit/<int:id>/', views.Itemedit, name='itemedit'),

    #sitterregistration
    path('sittersform/', views.sittersform, name='sittersform'),
    path('sitterslist/', views.sitterslist, name='sitterslist'),
    path('sitterview/<int:id>/',views.sitterview,name='sitterview'),
    path('sarrivalview/<int:id>/',views.sarrivalview,name='sarrivalview'),
    path('spayment/',views.spayment, name='spayment'),
    path('spaymentlist/',views.spaymentlist, name='spaymentlist'),
    path('sittersedit/<int:id>/', views.sittersedit, name='sittersedit'),
    path('sarrivaledit/<int:id>/', views.sarrivaledit, name='sarrivaledit'),
    path('sarrival/',views.sarrival, name='sarrival'),
    path('sarrivallist/',views.Sarrivallist, name='sarrivallist'),
    path('sitter/<int:id>/delete/',views.sitterdelete, name='sitterdelete'),
    path('sarrival/<int:id>/delete/',views.sarrivaldelete, name='sarrivaldelete'),
    path('sitters/', views.sitter_list_view, name='sitters'),
    

    #babyregistration
    path('babesform/', views.babesform, name='babesform'),
    path('babyslist/',views.babyslist, name='babyslist'),
    path('babyview/<int:id>/',views.babyview,name='babyview'),
    path('babyedit/<int:id>/',views.babyedit,name='babyedit'),
    path('baby/<int:id>/delete/',views.babydelete, name='babydelete'),
    # path('itemview/<int:id>/',views.sitterview, name='itemview'),
    # path('shopstockedit/<int:id>/',views.shopstockedit, name='shopstockedit'),
    path('bpayment/',views.bpayment, name='bpayment'),
    #babypayment
    # path('baby/<int:id>/delete/',views.babydelete, name='babydelete'),
    # path('baby/', views.baby_list_view, name='baby'),
]
