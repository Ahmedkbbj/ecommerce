from django.shortcuts import render
from .models import Product, Category
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from ecommerce.functions import pack
# Create your views here.

def homeview(request):

    last_products = Product.objects.all().order_by('-created_at')[:8]

    featured_products = Product.objects.filter(featured=True)

    best_products = sorted(Product.objects.all(), key=lambda p: p.nb_order, reverse = True)[:8]
    context = {"last_products":last_products ,"best_products":best_products, "featured_products": featured_products}

    return render(request, "pages/home.html", context)

import random
def single_product_view(request, slug):
    # category = get_object_or_404(Category,name=slug)
    product = get_object_or_404(Product, slug=slug)
    top_products = list(Product.objects.all())
    len_of_products = 12 if len(top_products) >= 12 else len(top_products)
    top_products =  pack(list(top_products)) if len(top_products) == 12 else  pack(list(random.sample(top_products, 9) ))
    context = {'product':product, "top_products":top_products}

    return render(request, "pages/single_product.html", context)


def shopview(request, slug):

    category = get_object_or_404(Category,name=slug)

    products = Product.objects.filter(category=category)

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


    context = {"products":products}


    return render(request, "pages/shop.html",context)

from .forms import ClientForm
from django.views import View
from django.http import JsonResponse
class save_order(View):

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        product = get_object_or_404(Product, slug=slug)
        top_products = list(Product.objects.all())
        len_of_products = 12 if len(top_products) >= 12 else len(top_products)
        top_products =  pack(list(top_products)) if len(top_products) == 12 else  pack(list(random.sample(top_products, 9) ))
        form = ClientForm()

        context = {'product':product, "top_products":top_products, "form":form}

        return render(request, "pages/single_product.html",context)

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'seccuss': "well sent"})
        
        return render(request, "pages/single_product.html", {"form":form})