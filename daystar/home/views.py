from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django import *
from . models import *
from .forms import *
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.
def index(request):
   return render(request,'index.html')
    

def reset_password(request):
   return render(request,'reset_password.html')   

def logout(request):
   return render(request,'logout.html') 

def arrival(request):
    if request.method == 'POST':
        form = AddArrival(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            messages.success(request, 'Baby added successfully')
            return redirect('arrivallist')
    else:
        form = AddArrival()
    return render (request, 'arrival.html',{'form':form})

def sarrival(request):
    if request.method == 'POST':
        form = AddSarrival(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            messages.success(request, 'Sitter added successfully')
            return redirect('sarrivallist')
    else:
        form = AddSarrival()
    return render (request, 'sarrival.html',{'form':form})
         

def dash(request):
   return render(request,'dash.html')  


         
   

def bdeparture(request):
   if request.method == 'POST':
      form=AddBdeparture(request.POST)
      if form.is_valid():
         form.save()
         print(form)
         messages.success(request, 'Baby added successfully')
         return redirect('bdeparturelist')
   else:
      form = AddBdeparture()
   return render(request,'bdeparture.html',{'form':form})



def bpayment(request):
   bpayment = AddBpayment
   return render (request, 'bpayment.html', {'bpayment':bpayment})

def bpayment(request):
        if request.method == 'POST':
            form = AddBpayment(request.POST)
            if form.is_valid():
                form.save()
                return redirect('bpaymentlist')  
        else:
            form = AddBpayment()
        return render(request, 'bpayment.html', {'form': form})


def spayment(request):
        if request.method == 'POST':
            form = AddSpayment(request.POST)
            if form.is_valid():
                form.save()
                return redirect('spaymentlist')  
        else:
            form = AddSpayment()
        return render(request, 'spayment.html', {'form': form})
        
def login(request):
   return render (request, 'login.html')

def bdeparturelist(request):    
   bdeparturelist = B_departure.objects.all()
   return render (request, 'bdeparturelist.html',{'bdeparturelist':bdeparturelist})


   
def arrivallist(request):
   arrivallist = Arrival.objects.all()
   return render (request, 'arrivallist.html',{'arrivallist':arrivallist})

def sarrivallist(request):
   sarrivallist = Sarrival.objects.all()
   return render (request, 'sarrivallist.html',{'sarrivallist':sarrivallist})





def logout(request):
    logout(request)
    return redirect('index')
    getbabeform = AddBabe()
    return render(request,'sitters/logout.html',{'getlogout':getlogout})
#sitterregistration form
def sittersform(request):
    if request.method == 'POST':
        form = AddSitter(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            messages.success(request, 'sitter added successfully')
            return redirect('sitterslist')
    else:
        form = AddSitter()
    return render(request,'sittersform.html',{'form':form})
def sitterslist(request):
   sitterslist = Sittersform.objects.all()
   return render (request, 'sitterslist.html',{'sitterslist':sitterslist})

def spaymentlist(request):
   spaymentlist = Spayment.objects.all()
   return render (request, 'spaymentlist.html',{'spaymentlist':spaymentlist})

def bpaymentlist(request):
   bpaymentlist = Bpayment.objects.all()
   return render (request, 'bpaymentlist.html',{'bpaymentlist':bpaymentlist})


def sittersedit(request,id):
    sitter=get_object_or_404(Sittersform,id=id)
    if request.method == 'POST':
       form=AddSitter(request.POST,instance=sitter)
       if form.is_valid():
           form.save()
           return redirect('sitterslist')
    else:
        form=AddSitter(instance=sitter)
    return render(request,'sittersedit.html',{'form':form,'sitter':sitter})
    
# def sittersdelete(request,id):
#     sitter=get_object_or_404(Sittersform,id=id)
#     if request.method == 'POST':
#        form=AddSitter(request.POST,instance=sitter)
#        if form.is_valid():
#            form.save()
#            return redirect('sitterslist')
#     else:
#         form=AddSitter(instance=sitter)
#     return render(request,'sittersdelete.html',{'form':form,'sitter':sitter})

def  sitterview(request,id):
    sitter_info=Sittersform.objects.get(id=id)   
    return render(request,'sitterview.html',{'sitter_info':sitter_info})
#babyregistration
def babesform(request):
   if request.method == 'POST':
      form=AddBabe(request.POST)
      if form.is_valid():
         form.save()
         print(form)
         messages.success(request, 'Baby added successfully')
         return redirect('babyslist')
   else:
      form = AddBabe()
   return render(request,'babesform.html',{'form':form})

def babyslist(request):
   babyslist = Babesform.objects.all()
   return render (request, 'babyslist.html',{'babyslist':babyslist})

def babyedit(request,id):
    baby=get_object_or_404(Babesform,id=id)
    if request.method == 'POST':
       form=AddBabe(request.POST,instance=baby)
       if form.is_valid():
           form.save()
           return redirect('babyslist')
    else:
        form=AddBabe(instance=baby)
    return render(request,'babyedit.html',{'form':form,'baby':baby})

def  babyview(request,id):
    baby_info=Babesform.objects.get(id=id)   
    return render(request,'babyview.html',{'baby_info':baby_info})
    
#dollscorner
def dollscorner(request, dolls_id):
    dolls = get_object_or_404(Doll, id=dolls_id)
    return render(request, 'dollscorner.html', {'dolls': dolls})

@login_required
def receipt(request):
    sales= Salesrecord.objects.all().order_by('-id') 
    return render(request,'receipt.html',{'sales':sales})  
@login_required
def issue_item(request,pk):
    issued_item=Doll.objects.get(id=pk) 
    sales_form=SalesrecordForm(request.POST)  

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale=sales_form.save(commit=False)
            new_sale.doll=issued_item
            new_sale.unit_price=issued_item.Unit_price
            new_sale.save()
            issued_quantity=int(request.POST['quantity_sold'])
            issued_item.quantity-=issued_quantity
            issued_item.save()
            print(issued_item.name_of_the_doll)
            print(request.POST['quantity_sold'])
            print(issued_item.quantity)
            return redirect('receipt')
    return render(request, 'issue_item.html',{'sales_form':sales_form} )

@login_required
def receipt_detail(request, receipt_id):
            receipt = Salesrecord.objects.get(id=receipt_id)
            return render(request,'receipt_detail.html',{'receipt':receipt})




@login_required
def add_to_stock(request, pk):
    issued_item = Doll.objects.get(id=pk)
    if request.method == 'POST':
        form = Addform(request.POST)
        if form.is_valid():
            received_quantity = request.POST.get('received_quantity')
            if received_quantity:
                try:
                    added_quantity = int(received_quantity)
                    issued_item.quantity += added_quantity
                    issued_item.save()
                    print(added_quantity)
                    print(issued_item.quantity)
                    return redirect('doll')
                except ValueError:
                    return HttpResponseBadRequest("Invalid quantity")
    else:
        form = Addform()
    return render(request, 'add_to_stock.html', {'form': form})



@login_required
def all_sales(request):
    sales=Salesrecord.objects.all()
    total=sum([items.amount_received for items in sales])
    change=sum([items.get_change() for items in sales])
    net=total-change
    return render(request,'all_sales.html',{'sales':sales,'total':total,'change':change,'net':net})

def doll(request):
    dolls=Doll.objects.all()
    return render(request,'doll.html',{'dolls':dolls})

def shopform(request):
   if request.method == 'POST':
      form=AddShop(request.POST)
      if form.is_valid():
         form.save()
         print(form)
         messages.success(request, 'Baby added successfully')
         return redirect('shopstock')
   else:
      form = AddShop()
   return render(request,'shopform.html',{'form':form})

def shopstock(request):
   shopstock = Shopform.objects.all()
   return render (request, 'shopstock.html',{'shopstock':shopstock})
