# Generated by Django 4.2.7 on 2023-12-21 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0016_rename_delivery_address_deliveryaddress_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='house_number',
            field=models.CharField(max_length=100),
        ),
    ]