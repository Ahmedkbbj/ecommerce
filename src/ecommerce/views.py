from django.shortcuts import render
from .models import Product
# Create your views here.

def homeview(request):

    last_products = Product.objects.all().order_by('created_at')

    context = {"last_products":last_products }

    


    return render(request, "pages/home.html", context)