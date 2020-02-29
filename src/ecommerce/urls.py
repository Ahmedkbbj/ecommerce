from django.urls import path
from .views import homeview, single_product_view, shopview, save_order, single_product_view, about_us, contact_us, save_order_offre

app_name = 'ecommerce'


urlpatterns = [
    path('', homeview, name="home"),
    path('products/<slug:slug>/', single_product_view , name="single-product"),
    path('order/save/<slug:slug>/', save_order.as_view() , name="save_order"),
    path('order/offre/save/', save_order_offre.as_view() , name="save_order_offre"),
    path('category/<slug:slug>/', shopview , name="shop-product"),
    path('about/', about_us , name="about_us"),
    path('contact/', contact_us , name="contact_us"),

]