from django.db import models

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



class Product(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    created_at = models.DateField()



class Galery(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)


class Command(models.Model):

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField()