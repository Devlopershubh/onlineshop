# Generated by Django 4.2.6 on 2023-11-20 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomapp', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecomapp.category'),
        ),
    ]
