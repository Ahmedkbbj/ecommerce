# Generated by Django 2.2 on 2020-02-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='/static/img/default.jpg', null=True, upload_to=''),
        ),
    ]
