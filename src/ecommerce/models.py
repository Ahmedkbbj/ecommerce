from django.db import models
import hashlib 
from django.urls import reverse
from django_countries.fields import CountryField
from django.utils import timezone
GENDER = (
        ('',"Sex"),
        ('M',"MAN"),
        ('W',"WOMAN")
    )

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    country = CountryField(blank_label='(select country)', null=True)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)
    created_at = models.DateField(default=timezone.now)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    slug = models.CharField(max_length=50, null=True)

    def get_absolute_url(self):
        return reverse('ecommerce:shop-product', args=[self.name.replace(" ", "-")])

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField(null=True)
    image = models.ImageField(null=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=50, null=True)
    width = models.FloatField(null=True,blank=True)
    height = models.FloatField(null=True,blank=True)
    depth = models.FloatField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    created_at = models.DateField(null=True,blank=True, default=timezone.now)
    
    @property
    def nb_order(self):
        number_order = len(Order.objects.filter(product=self))
        return number_order

    def generate_hash(self):
        result = hashlib.md5(str(self.pk).encode())
        return self.name.replace(" ", "-")+"-"+str(result.hexdigest())

    def get_absolute_url(self):
        return reverse('ecommerce:single-product', args=[self.slug])
    

    def get_gallery_product(self):
        images = Galery.objects.filter(product=self)
        return images
    
    def len_image_in_gallery(self):
        return [i for i in range(4 - len(self.get_gallery_product()))]
    




    def __str__(self):
        return self.slug

class Galery(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)


class Order(models.Model):

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(default=timezone.now)


class SocialMedia(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField()