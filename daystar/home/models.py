
from django.db import models
from django.utils import timezone

class Categorystay(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class  Assigning_babies  (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  

   
class Sittersform(models.Model):
    sitter_name = models.CharField(max_length=200,)
    age = models.CharField(max_length=200, default=0)
    contact = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=200)
    level_of_education = models.CharField(max_length=50)
    nin = models.CharField(max_length=200)
    date_of_birth = models.DateField(max_length=200, default=0)
    # Assigning_babies = models.ForeignKey(Babesform,on_delete=models.CASCADE)

    def __str__(self):
        return self.sitter_name

class Sarrival(models.Model):
    sitter_names = models.ForeignKey(Sittersform,on_delete=models.CASCADE)
    timein = models.TimeField(default=timezone.now)
    sittersno = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now) 

    def __str__(self):
        return self.sitter_names

  
class Sitter(models.Model):
    name = models.CharField(max_length=100)
class Spayment(models.Model):
    name = models.ForeignKey(Sittersform,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=0, default=3000)
    date = models.DateField(default=timezone.now)
    numbers_of_babies_attended_to = models.IntegerField(default=0)

    def __str__(self):
        return str(self.amount)

    @property
    def total_amount_paid(self):
        # print("Amount:", self.amount)
        # print("Number of Babies Attended To:", self.numbers_of_babies_attended_to)
        return self.amount * self.numbers_of_babies_attended_to
    

class Babesform(models.Model):
    # c_stay = models.ForeignKey(Categorystay,on_delete=models.CASCADE,max_length=200)
    category_stay=models.CharField(max_length=200)
    baby_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200, default=0)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=50, null=True, default=None)
    sponsor = models.CharField(max_length=200)
    parentsname = models.CharField(max_length=200)
    babysno = models.CharField(max_length=200, default=0)
    timein = models.DateTimeField()
    brought_by = models.CharField(max_length=200)
   

    def __str__(self):
        return self.baby_name

class B_departure(models.Model):
    baby_names = models.ForeignKey(Babesform,on_delete=models.CASCADE)
    person_taking_baby = models.CharField(max_length=200)
    telephone_no = models.CharField(max_length=200)
    timeout = models.DateTimeField()
    babyno = models.IntegerField(default=0)
    comments = models.TextField(max_length=500)

    def __str__(self):
        return self.b_names

class  category_payment_id(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  
class Bpayment(models.Model):
    category_payment_id = models.ForeignKey(Categorystay, on_delete=models.CASCADE, max_length=200)
    Payno = models.IntegerField(default=0)
    currency = models.IntegerField(default=0, choices=[(10000, '10000'), (15000, '15000'), (300000, '300000'), (450000, '450000')])
    amount_paid = models.IntegerField(default=0)
    payee=models.ForeignKey(Babesform,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.payee

    def get_balance(self):
        return self.currency - self.amount_paid

        


class Category_doll(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name      

class Doll(models.Model):
    category_doll = models.ForeignKey(Category_doll, on_delete=models.CASCADE, null=True, blank=True)
    name_of_the_doll = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    issued_quantity = models.IntegerField(default=0, blank=True, null=True) 
    received_quantity = models.IntegerField(default=0, null=True, blank=True)
    Unit_price = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def _str_(self):
        return self.name_of_the_doll

class Salesrecord(models.Model):    
    doll = models.ForeignKey(Doll, on_delete=models.CASCADE, null=False, blank=False)
    payee = models.ForeignKey(Babesform, on_delete=models.CASCADE, null=True, blank=True)
    quantity_sold = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    sale_date = models.DateField(default=timezone.now, null=True, blank=True)
    unit_price = models.IntegerField(default=0)

    def get_total(self):
        # Ensure that `quantity_sold` and `unit_price` are not None
        quantity = self.quantity_sold if self.quantity_sold is not None else 0
        unit_price = self.unit_price if self.unit_price is not None else 0
        total = quantity * unit_price
        return int(total)

    def get_change(self):
        # Ensure that `amount_received` is not None
        total = self.get_total()
        amount_received = self.amount_received if self.amount_received is not None else 0
        change = total - amount_received
        return int(change)

      



class Shopform(models.Model):
    ITEM_CHOICES = (
        ('Fruits', 'Fruits'),
        ('Diapers', 'Diapers'),
        ('Milk', 'Milk'),
        ('Toys', 'Toys'),
    )
    baby_names = models.ForeignKey(Babesform, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=100, choices=ITEM_CHOICES)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    Date_of_purchase = models.DateField(default=timezone.now)
    unit_price = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name
    
    
class shopStock(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name      

    