# Generated by Django 2.2 on 2020-01-11 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_auto_20200111_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]