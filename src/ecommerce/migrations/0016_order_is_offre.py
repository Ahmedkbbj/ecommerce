# Generated by Django 2.2 on 2020-02-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_auto_20200229_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_offre',
            field=models.BooleanField(default=False),
        ),
    ]
