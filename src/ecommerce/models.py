from django.db import models
import hashlib 
from django.urls import reverse

GENDER = (
    ('W','W'),
    ('M','M')
)

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    created_at = models.DateField()


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.CharField(max_length=50, null=True)

    def get_absolute_url(self):
        return reverse('products:shop-product', args=[self.name.replace(" ", "-")])

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField(null=True)
    image = models.ImageField(null=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=50, null=True)
    created_at = models.DateField()
    
    @property
    def nb_order(self):
        number_order = len(Order.objects.filter(product=self))
        return number_order

    def generate_hash(self):
        result = hashlib.md5(str(self.pk).encode())
        return self.name.replace(" ", "-")+"-"+str(result.hexdigest())

    def get_absolute_url(self):
        return reverse('products:single-product', args=[self.slug])


class Galery(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)


class Order(models.Model):

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField()