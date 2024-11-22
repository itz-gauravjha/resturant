from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem
# Register your models here.

class CartItemAdmin(admin.StackedInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
    ]
    inlines = [CartItemAdmin]

admin.site.register(Cart, CartAdmin)

admin.site.register(Order)
admin.site.register(OrderItem)