from django.db import models
import hashlib 
from django.urls import reverse
from django_countries.fields import CountryField
from django.utils import timezone
from django.utils.html import mark_safe
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


    def __str__(self):
        return self.first_name +" " + self.last_name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField( default="/default.jpg")
    slug = models.CharField(max_length=50, null=True)

    def get_absolute_url(self):
        return reverse('ecommerce:shop-product', args=[self.name.replace(" ", "-")])

    # def __str__(self):
    #     return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField(null=True)
    image = models.ImageField(default="/default.jpg")
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=50, null=True)
    width = models.FloatField(null=True,blank=True)
    height = models.FloatField(null=True,blank=True)
    depth = models.FloatField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    created_at = models.DateField(null=True,blank=True, default=timezone.now)
    

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = 'Image'
    def __str__(self):
        return self.name

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
    image = models.ImageField(default="/default.jpg")
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)


class Order(models.Model):

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    is_offre = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    def image_tag(self):
        image = None
        if self.product:
            image = mark_safe('<img src="%s" width="150" height="150" />' % (self.product.image.url))
        return image

    # def __str__(self):
    #     return str(self.client) + "   /   " + self.product + "  /  " + self.is_offre + "  /  "+ self.created_at

class SocialMedia(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(default="/default.jpg")
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name 

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))


class Offer(models.Model):
    
    title = models.CharField(max_length=50,default="Up To 50% Off")
    descriptions = models.TextField(default="Him she'd let them sixth saw light")
    image = models.ImageField(default="/default.jpg")

    def __str__(self):
        return self.title
    