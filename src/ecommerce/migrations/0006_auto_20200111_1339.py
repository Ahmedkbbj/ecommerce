# Generated by Django 2.2 on 2020-01-11 12:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20200111_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 11, 12, 39, 13, 717878, tzinfo=utc), null=True),
        ),
    ]