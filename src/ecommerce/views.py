from django.shortcuts import render
from .models import Product
# Create your views here.

def homeview(request):

    last_products = Product.objects.all().order_by('created_at')
    last_products = last_products[2] if last_products.exists() else []

    products = Product.objects.exclude(pk__in=[item.pk for item in last_products]) 
    products = products[7] if products.exists() else Product.objects.all()

    


    return render(request, "pages/home.html", {})