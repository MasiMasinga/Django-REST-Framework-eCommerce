from django.contrib import admin # type: ignore
from .models import Product, Review, Order, OrderItem, ShippingAddress

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

class ReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Review._meta.fields]

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ShippingAddress._meta.fields]

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)

