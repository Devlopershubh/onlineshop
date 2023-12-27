

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', views.home, name="home"),
    path('about/', views.about),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout' ),
    path('account/<int:id>', views.account ,name='account'),
    path('category/', views.showcategory,name='category'),
    path('products/', views.products,name='products'),
    path('product/<int:id>', views.showProductsById,name='product'),
    path('details/<int:id>', views.productdetails,name='details'),
    path('cart/', views.cart, name='cart'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
  
    path('deleteCartItmes/', views.deleteCartItmes, name='deleteCartItmes'),
    path('placeorder/', views.placeorder,name='placeorder'),
    path('checkout_address/',views.checkout_address,name='checkout_address'),

    path('add_address/', views.add_address,name='add_address'),
    path('checkout/',views.checkout,name='checkout'),
    path('checkout_update/',views.checkout_update,name='checkout_update'),
    path('payment/',views.payment,name='payment'),
   
    path('updateCartItems/', views.updateCartItmes, name='updateCartItmes'),
    path('myorder/',views.myorder,name='myorder'),
    path('trackorder/',views.trackorder, name='trackorder')

    

    

   




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
