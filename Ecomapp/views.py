from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from .forms import cartform,checkoutForm,addressForm,deliveryAddress
from django.contrib.auth.decorators import login_required 

from .models import Products, category, cartData, billing

def home(request):
    data= Products.objects.all()
    context= {'data': data}

    return render(request, 'Ecomapp/index.html', context)

def about(request):
    return render(request, 'Ecomapp/about.html')
def signup(request):
    form=UserCreationForm()
    context={'form':form}

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'Ecomapp/signup.html',context)

def showcategory(request):
    data= category.objects.all()
    context ={'data': data}
    return render(request, 'Ecomapp/category.html', context)

def products(request):
    data= Products.objects.all()
    context ={'data': data}
    return render(request, 'Ecomapp/product.html', context)

def showProductsById(request, id):
    data= Products.objects.filter(category=id)
    context ={'data': data}
    return render(request, 'Ecomapp/product.html', context)

def productdetails(request, id):
    data= Products.objects.get(id=id)

    catid= data.category
    related= Products.objects.filter(category=catid)

    print(related)

    context ={'data': data, 'related': related}
    return render(request, 'Ecomapp/details.html', context)

def login(request): 
    form= AuthenticationForm()
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():

            username= request.POST['username']
            password= request.POST['password']

            user= authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request, user)
                return redirect('account',user.id)
    return render(request, 'Ecomapp/login.html')


def user_logout(request):
     logout(request)
     return redirect("Ecomapp/index.html")


def account(request,id):
    return render(request, 'Ecomapp/account.html')

def cart(request):

    # cart= cart.objects.filter(user= request.user)
    cart= cartData.objects.filter(user= request.user)
    cartTotal=0
    for x in cart:
             qty= x.qty
             pric= x.productId.price
             cartTotal+= qty*pric
       
             shipping=50
    
             totalamount=cartTotal+shipping   
                
             
             
    context= {'data': cart, 'total': cartTotal, 'totalAmount':totalamount,'shippingCharges':shipping}

    return render(request, 'Ecomapp/cart.html', context)


def add_to_cart(request):
    if request.method=="POST":
        productid = request.POST.get('productId')
        form=cartform(request.POST)


        if form.is_valid():
            existing_item = cartData.objects.filter(user =request.user, productId=productid).first()

            if existing_item:
                existing_item.qty +=1
                existing_item.save()
            else:
                form.save()
                return redirect('cart')
    
    # return render(request,'Ecomapp/cart.html')
    return redirect('cart')



def deleteCartItmes(request):
    if request.method=='POST':
        cartid = request.POST.get('productId')
        cart=  cartData.objects.get(user= request.user, id= cartid)
        cart.delete()
     
        return redirect('cart')
    
# def myorders(request):
#     return render(request, 'Ecomapp/myorders.html')

def placeorder(request):
    return render(request, 'Ecomapp/placeorders.html')

def add_address(request):
    return render(request, 'Ecomapp/add_address.html')

@login_required
def checkout(request):
       cartid= cartData.objects.filter(user= request.user)

       totalAmount=0
       for x in cartid:
             qty=x.qty
             totalAmount +=x.productId.price*qty
            
       try:
        customer = billing.objects.get(user=request.user)
       except billing.DoesNotExist:
        customer = None 
     

       lst=[]
       for x in cartid:
              lst.append(x.productId.id)
       idstring = ', '.join(map(str, lst))
       
       context= {'cp': idstring, 'customer': customer , 'cartid':cartid, 'totalAmount': totalAmount}

       form = checkoutForm()
       if request.method == 'POST':
            form=checkoutForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('payment')
              
       return render(request,'Ecomapp/checkout.html', context)


@login_required
def checkout_update(request):
     
       customer= billing.objects.get(user= request.user)
       context= { 'customer': customer}

       form = checkoutForm()
       if request.method == 'POST':
            form=checkoutForm(request.POST, instance=customer)
            if form.is_valid():
                  form.save()
                  return redirect('payment')

       return render(request,'shopapp/checkout.html', context)
                   


@login_required
def payment(request):
      
      return render(request, 'shopapp/payment.html')

# @login_required
# def myorder(request):
     
#       pl=[]
#       cart= billing.objects.filter(user= request.user)
#       for x in cart:
#               productList= x.CartData.split(',')

      
#       for x in productList:
#               pro= products.objects.get(id=x)
#               pl.append(pro)
       

#       context={"myorder": cart, 'data': pl}
#       return render(request, 'Ecomapp/myorder.html', context)

def updateCartItmes(request):
    if request.method=='POST':
        cartid = request.POST.get('productId')
        cart=  cartData.objects.get(user= request.user, id= cartid)
        cart.qty= request.POST['qty']
        cart.save()
     
        return redirect('cart')
    

@login_required
def checkout_address(request):
     
       customer= billing.objects.get(user= request.user)
       context= { 'customer': customer}

       form = checkoutForm()
       if request.method == 'POST':
            form=checkoutForm(request.POST, instance=customer)
            if form.is_valid():
                  form.save()
                  return redirect('payment')

       return render(request,'Ecomapp/checkout.html', context)
                   
@login_required
def delivery_address(request):
       form = addressForm()
       context ={'form': form}

       if request.method=='POST':
              form = addressForm(request.POST)
              if form.is_valid():
                     form.save()
                     return redirect('place_order')
       return render (request,'Ecomapp/aadaddress.html',context)

@login_required
def myorder(request):
     
      pl=[]
      cart= billing.objects.filter(user= request.user)
      for x in cart:
              productList= x.CartData.split(',')
    
      print(productList)
      
      for x in productList:
              pro=Products.objects.get(id=x)
              pl.append(pro)
       

      context={"myorder": cart, 'data': pl}
      return render(request, 'Ecomapp/myorder.html', context)

def trackorder(request):
     return render(request, 'Ecomapp/trackorder.html')