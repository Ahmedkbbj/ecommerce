from django.urls import path
from .views import homeview, singleview, shopview

app_name = 'products'


urlpatterns = [
    path('', homeview),
    path('products/<slug:slug>/', singleview , name="single-product"),
    path('category/<slug:slug>/', shopview , name="shop-product")

]