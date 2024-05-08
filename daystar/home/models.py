from django.db import models
from django.utils import timezone

# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Categorystay(models.Model):
      name = models.CharField(max_length=100) 
      def __str__(self):
         return self.name  


class Bpayment(models.Model):
    c_payment_id = models.ForeignKey(Categorystay, on_delete=models.CASCADE,max_length=200)
    amount = models.CharField(max_length=10, default='Ugx')
    Payno = models.CharField( max_length=200,default=0)
    currency = models.CharField(max_length=10, default='Ugx')

    def __str__(self):
        return self.amount

class Sitter_arrival(models.Model):
      name = models.CharField(max_length=100) 
      def __str__(self):
         return self.name   
 
class Sitterpayment(models.Model):
    sitter_name = models.ForeignKey(Sitter_arrival, on_delete=models.CASCADE)
    amount = models.CharField(max_length=10, default=3000 )
    date = models.DateField(default=timezone.now)
    numbers_of_babies_attended_to = models.IntegerField(default=0)
  
    def __str__(self):
        return f"Sitter Payment - {self.sitter_name} - Amount: {self.amount} - Date: {self.date}"
def calculation(self):
    cal= self.amount * self.numbers_of_babies_attended_to
    return int(cal)

    class Categorystay(models.Model):
      name = models.CharField(max_length=100) 
      def __str__(self):
         return self.name  

class Babesform(models.Model):
    c_stay = models.ForeignKey(Categorystay,on_delete = models.CASCADE,max_length=200)
    b_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200, default = 0)
    gender = models.CharField( max_length=100)
    location = models.CharField(max_length=50, null=True, default=None)
    sponsor = models.CharField(max_length=200)
    date = models.DateField(max_length=200,default=0)
    parentsname = models.CharField(max_length=200)
    babysno =models.CharField(max_length=200, default=0)
    timein = models.DateTimeField()
    person_bringing_baby = models.CharField(max_length=200)



    
    def __str__(self):
        return self.b_name
# Create your models here.




class Sittersform(models.Model):
    s_name = models.CharField(max_length=200,)
    age = models.CharField(max_length=200, default = 0)
    contact = models.CharField(max_length=200)
    gender = models.CharField( max_length=100)
    religion = models.CharField( max_length=100)
    location = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=200)
    level_of_education = models.CharField(max_length=50)
    nin= models.CharField(max_length=200)
    date_of_birth = models.DateField(max_length=200,default=0)

    
    def __str__(self):
        return self.s_name


class B_departure(models.Model):
    b_name = models.CharField(max_length=200)
    person_taking_baby = models.CharField(max_length=200)
    telephone_no = models.CharField(max_length=200)
    timeout = models.DateTimeField()
    babyno = models.IntegerField(default=0)
    comments = models.TextField(max_length=500)


    
    def __str__(self):
        return self.b_name


        
class Sarrival(models.Model):
    s_name = models.CharField(max_length=200)
    timein = models.TimeField(default=timezone.now)
    sittersno = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now) 
    
    
    def __str__(self):
        return self.s_name
class Category_doll(models.Model):
      name = models.CharField(max_length=100) 
      def __str__(self):
         return self.name      

class Doll(models.Model):
    c_doll=models.ForeignKey(Category_doll, on_delete=models.CASCADE,null=True, blank=True)
    name_of_the_doll =models.CharField(max_length=200,null=True, blank=True)
    quantity=models.IntegerField(default=0)
    doll_type=models.CharField(max_length=200, null=True,blank=True)
    issued_quantity=models.IntegerField(default=0,blank=True,null=True) 
    received_quantity=models.IntegerField(default=0,null=True,blank=True)
    Unit_price=models.IntegerField(default=0,null=True, blank=True)
    date=models.DateField(default=timezone.now)
    def _str_(self):
        return self.name_of_the_doll
    

class Salesrecord(models.Model):    
    doll=models.ForeignKey(Doll,  on_delete=models.CASCADE,null=False, blank=False)
    payee=models.ForeignKey(Babesform, on_delete=models.CASCADE,null=False,blank=False)
    quantity_sold=models.IntegerField(default=0)
    amount_received=models.IntegerField(default=0)
    sale_date=models.DateField(default=timezone.now)
    unit_price=models.IntegerField(default=0)
     
    def get_total(self):
            total= self.quantity_sold * self.unit_price
            return int( total)
    #here we are getting change.(money to be given to theparent)    
    def get_change(self):
            change= self.get_total() - self.amount_received
            return int(change)#sales is linked to products


