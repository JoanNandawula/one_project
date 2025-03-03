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

def login(request):
   return render (request, 'login.html')

def dash(request):
   return render(request,'dash.html')  

def logout(request):
    logout(request)
    return redirect('index')
    getbabeform = AddBabe()
    return render(request,'sitters/logout.html',{'getlogout':getlogout})

# def arrival(request):
#     if request.method == 'POST':
#         form = AddArrival(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form)
#             messages.success(request, 'Baby added successfully')
#             return redirect('arrivallist')
#     else:
#         form = AddArrival()
#     return render (request, 'arrival.html',{'form':form})


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


def bdeparturelist(request):    
   bdeparturelist = B_departure.objects.all()
   return render (request, 'bdeparturelist.html',{'bdeparturelist':bdeparturelist})

def bpaymentlist(request):
   bpaymentlist = Bpayment.objects.all()
   return render (request, 'bpaymentlist.html',{'bpaymentlist':bpaymentlist})

    
#babyregistration
@login_required
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

@login_required
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

@login_required
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




@login_required
def bdepartureedit(request,id):
    baby=get_object_or_404(Babesform,id=id)
    if request.method == 'POST':
       form=AddShop(request.POST,instance=baby)
       if form.is_valid():
           form.save()
           return redirect('babyslist')
    else:
        form=AddShop(instance=baby)
    return render(request,'bdepartureedit.html',{'form':form,'baby':baby})
    
def  bdepartureview(request,id):
    baby_info=B_departure.objects.get(id=id)   
    return render(request,'bdepartureview.html',{'baby_info':baby_info})


def spayment(request):
        if request.method == 'POST':
            form = AddSpayment(request.POST)
            if form.is_valid():
                form.save()
                return redirect('spaymentlist')  
        else:
            form = AddSpayment()
        return render(request, 'spayment.html', {'form': form})
        


def Sarrivallist(request):
    sarrivallist = Sarrival.objects.all()  # Retrieve all instances of Sarrival
    return render(request, 'sarrivallist.html', {'sarrivallist': sarrivallist})





#sitterregistration form
@login_required
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
   spaymentlist= Spayment.objects.all()
   return render (request, 'spaymentlist.html',{'spaymentlist':spaymentlist})
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


@login_required
def sittersedit(request,id):
    sitter=get_object_or_404(Sittersform)
    if request.method == 'POST':
       form=AddSitter(request.POST,instance=sitter)
       if form.is_valid():
           form.save()
           return redirect('sitterslist')
    else:
        form=AddSitter(instance=sitter)
    return render(request,'sittersedit.html',{'form':form,'sitter':sitter})




def  sitterview(request,id):
    sitter_info=Sittersform.objects.get(id=id)   
    return render(request,'sitterview.html',{'sitter_info':sitter_info})

def  sarrivalview(request,id):
    sitter_info=Sarrival.objects.get(id=id)   
    return render(request,'sarrivalview.html',{'sitter_info':sitter_info})

@login_required
def sarrivaledit(request,id):
    sitter=get_object_or_404(Sarrival,id=id)
    if request.method == 'POST':
       form=AddSarrival(request.POST,instance=sitter)
       if form.is_valid():
           form.save()
           return redirect('sarrivallist')
    else:
        form=AddSarrival(instance=sitter)
    return render(request,'sarrivaledit.html',{'form':form,'sitter':sitter})

def sitterdelete(request, id):
    sitter = get_object_or_404(Sittersform, id=id)
    
    if request.method == 'POST':
        sitter.delete()
        return redirect('sitterslist')
    
    return redirect('sitterslist')


def sarrivaldelete(request, id):
    sitter = get_object_or_404(Sittersform, id=id)
    
    if request.method == 'POST':
        sitter.delete()
        return redirect('sarrivallist')
    
    return redirect('sarrivallist')
    
   
@login_required
def Itemedit(request,id):
    item=get_object_or_404(Shopform,id=id)
    if request.method == 'POST':
       form=AddShop(request.POST,instance=item)
       if form.is_valid():
           form.save()
           return redirect('shopstock')
    else:
        form=AddShop(instance=item)
    return render(request,'itemedit.html',{'form':form,'item':item}) 
    

    

    
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
@login_required
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
    return render(request, 'shopstock.html', {'shopstock': shopstock})


def babydelete(request, id):
    baby = get_object_or_404(Babesform, id=id)
    
    if request.method == 'POST':
        baby.delete()
        return redirect('babyslist')
    
    return redirect('babyslist')



def itemdelete(request, id):
    item = get_object_or_404(Shopform, id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('shopstock')
    
    return redirect('shopstock')

@login_required
def home(request):
    count_sitters = Sitter_registration.objects.count()
    count_babies_signed_out = Baby_departure.objects.filter(departure_time__date=date.today()).count()
    count_sitters_signed_in = Arrivalsitter.objects.filter(Arrival_Date__date=date.today()).count()
    count_babies_registered = Babie_registration.objects.filter(Arrival_Date=date.today()).count()
    count_babies_total = count_babies_registered - count_babies_signed_out
    context = {
        "count_sitters": count_sitters,  # Total sitters registered
        "count_babies": count_babies_total,  # Total babies currently signed in
        "count_babies_signed_out": count_babies_signed_out,  # Babies signed out today
        "count_sitters_signed_in": count_sitters_signed_in,}  # Sitters signed in today
        
    return render(request, "dash.html", context)

 

def sitter_list_view(request):
    form = SitterSearchForm(request.GET or None)
    query = request.GET.get('query')
    if query:
        sitterslist = Sittersform.objects.filter(sitter_name__icontains=query)  # Adjust the field as necessary
    else:
        sitterslist = Sittersform.objects.all()
    return render(request, 'sitterslist.html', {'sitterslist': sitterslist, 'form': form})

def baby_list_view(request):
    form = BabySearchForm(request.GET or None)
    query = request.GET.get('query')
    if query:
        babyslist = Babesform.objects.filter(sitter_name__icontains=query)  # Adjust the field as necessary
    else:
        sitterslist = Babesform.objects.all()
    return render(request, 'Babyslist.html', {'babyslist': babyslist, 'form': form})

def dashboard_view(request):
    sitter_count = Sitter.objects.count()  # Total count of all sitters
    return render(request, 'dashboard.html', {'sitter_count': sitter_count})
def shopstockview(request, id):
    item_info = Shopform.objects.get(id=id)
    return render(request, 'shopstockview.html', {'item_info': item_info})



