from django.shortcuts import render
from .models import Product, Category, Order, Offer
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from ecommerce.functions import pack, search_products

from .forms import ClientForm, ContactForm
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
# Create your views here.

def homeview(request):

    last_products = Product.objects.all().order_by('-created_at')[:8]

    featured_products = Product.objects.filter(featured=True)

    categorys = Category.objects.all()

    offre = Offer.objects.last()

    best_products = sorted(Product.objects.all(), key=lambda p: p.nb_order, reverse = True)[:8]
    context = {"last_products":last_products ,"best_products":best_products, "featured_products": featured_products, "offre":offre}
    context.update({"categorys":categorys})
    return render(request, "pages/home.html", context)

import random
def single_product_view(request, slug):
    # category = get_object_or_404(Category,name=slug)
    product = get_object_or_404(Product, slug=slug)
    top_products = list(Product.objects.all())
    len_of_products = 12 if len(top_products) >= 12 else len(top_products)
    top_products =  pack(list(top_products)) if len(top_products) == 12 else  pack(list(random.sample(top_products, len_of_products) ))
    context = {'product':product, "top_products":top_products}

    return render(request, "pages/single_product.html", context)


def shopview(request, slug):
    context = {}
    if slug != 'all' :
        category = get_object_or_404(Category,name=slug)
        products = Product.objects.filter(category=category)
        context.update({"slug":category.slug})
    else:
        products = Product.objects.all()

    if "search" in request.GET:
        search = request.GET.get('search','')
        slug_search = request.GET.get('search','')
        products = search_products(search, products)
    if products:
        page = request.GET.get('page', 1)

        paginator = Paginator(products, 6)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)


    context.update({"products":products})
    context.update({"slug":"all"})

    return render(request, "pages/shop.html",context)



class save_order(View):

    def get(self, request, *args, **kwargs):
        form = ClientForm()
        data = {}
        context = {"form":form}
        html_form = render_to_string('pages/client_form.html', context, request=request)
        return JsonResponse({'html_form': html_form})             

    def post(self, request, *args, **kwargs):
        slug_product = kwargs.get("slug","")
        form = ClientForm(request.POST or None)
        data = {}
        context = {"form":form}
        if form.is_valid():
            client = form.save()
            product = get_object_or_404(Product, slug=slug_product)
            Order.objects.create(client=client, product=product)
            data["form_is_valid"] = True
        else:
            data["form_is_valid"] = False
            
        
        data["html_form"] = render_to_string('pages/client_form.html', context, request=request)
        return JsonResponse(data)


class save_order_offre(View):

    def get(self, request, *args, **kwargs):
        form = ClientForm()
        data = {}
        context = {"form":form}
        html_form = render_to_string('pages/client_form.html', context, request=request)
        return JsonResponse({'html_form': html_form})             

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST or None)
        data = {}
        context = {"form":form}
        if form.is_valid():
            client = form.save()
            Order.objects.create(client=client, product=None, is_offre=True)
            data["form_is_valid"] = True
        else:
            data["form_is_valid"] = False
            
        
        data["html_form"] = render_to_string('pages/client_form.html', context, request=request)
        return JsonResponse(data)




def about_us(request):
    return render(request, 'pages/about_us.html')




def contact_us(request):
    form = ContactForm()
    print(request.POST)
    if request.POST:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            send_mail(
            'That’s your subject',
            'That’s your message body',
            'exemple@gmail.com',
            ['ahmed.kab20@gmail.com',],
            )
            

    return render(request, "pages/contact_us.html",{"form":form})



