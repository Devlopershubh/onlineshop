from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class category(models.Model):
    category_name =models.CharField(max_length=50)
    category_image =models.ImageField(upload_to= 'media/category')

    def __str__(self):
        return self.category_name


class Products(models.Model):

    name= models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    price= models.IntegerField()
    image= models.ImageField(upload_to='media/')
    category= models.ForeignKey(category, on_delete=models.CASCADE)
    code= models.CharField(max_length=100)
    description= models.TextField(null=True)
    
    def __str__(self):
        return self.title


class cartData(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    productId=models.ForeignKey(Products, on_delete=models.CASCADE)
    qty =models.PositiveBigIntegerField(default=1)
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return self.productId.name
    
class deliveryAddress(models.Model):
        User = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=50)
        mobile_number = models.CharField(max_length=15, validators=[])
        house_number = models.CharField(max_length=20)
        area = models.CharField(max_length=50)
        landmark = models.CharField(max_length=50)
        pincode = models.IntegerField()
        city = models.CharField(max_length=50)
        state = models.CharField(max_length=50)
        country = models.CharField(max_length=50)

        def __str__(self):
         return self.name
        

class billing(models.Model):
    user=models.ForeignKey (User,on_delete=models.CASCADE)
    CartData=models.CharField(max_length=200)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    house_number=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    pincode=models.IntegerField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    paymentMode=models.CharField(max_length=20)
    paymentStatus=models.BooleanField(default=False)
    orederDate=models.DateField(auto_now_add=True,null=True,editable=True)
    

    def __str__(self):
        return self.first_name
    


class trackorder(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    orderid=models.ForeignKey(billing, on_delete=models.CASCADE)
    orderStuts=models.TextField()
    orderStutsDate = models.DateTimeField(auto_now_add=True)