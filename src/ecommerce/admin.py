from django.contrib import admin
from .models import *

# Register your models here.

class OredreAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['client', 'product','image_tag', 'is_offre', "created_at"]


class ProductAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'price', 'image_tag', "featured", "category"]

class CategoryAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'image_tag']


class ClientAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['first_name', 'last_name', "email", "phone", "country","adress", "city", "age", "gender","created_at"]


class SocialMediaAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', "image_tag","url"]




admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OredreAdmin)
admin.site.register(Galery)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Offer)
