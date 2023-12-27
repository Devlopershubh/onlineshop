from django.contrib import admin

from .models import Products

admin.site.register(Products)

from .models import category,cartData,billing,deliveryAddress,trackorder


admin.site.register(category)
admin.site.register(cartData)
admin.site.register(billing)

admin.site.register(deliveryAddress)





