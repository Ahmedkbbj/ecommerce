from django.urls import path
from .views import homeview, single_product_view, shopview, save_order

app_name = 'products'


urlpatterns = [
    path('', homeview),
    path('products/<slug:slug>/', save_order.as_view() , name="single-product"),
    path('category/<slug:slug>/', shopview , name="shop-product")

]