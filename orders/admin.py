from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'adres')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'product', 'name', 'price', 'quantity', 'created_timestamp')
    list_filter = ('order_id', 'product')
    search_fields = ('name',)