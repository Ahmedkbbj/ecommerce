from django.shortcuts import render
from .models import Product, Category
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
# Create your views here.

def homeview(request):

    last_products = Product.objects.all().order_by('-created_at')[:3]

    featured_products = Product.objects.filter(featured=True)

    best_products = sorted(Product.objects.all(), key=lambda p: p.nb_order, reverse = True)[:3]
    context = {"last_products":last_products ,"best_products":best_products, "featured_products": featured_products}

    return render(request, "pages/home.html", context)


def singleview(request, slug):
    category = get_object_or_404(Category,name=slug)
    return render(request, "pages/single.html")


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

