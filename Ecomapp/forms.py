from .models import cartData,billing,deliveryAddress,trackorder

from django import forms


class cartform(forms.ModelForm):
             
            class Meta:
                    model = cartData
                    fields= '__all__'

class checkoutForm(forms.ModelForm):
    class Meta:
        model=billing 
        fields='__all__'

class addressForm(forms.ModelForm):
    class Meta:
        model=deliveryAddress
        fields='__all__'
    
# class OrderForm(forms.ModelForm):
#       class Meta:
#             model= Order
#             fields= "__all__"


class trackorder(forms.ModelForm):
      class Meta:
            model= trackorder
            fields= "__all__"