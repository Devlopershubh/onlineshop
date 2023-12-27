# Generated by Django 4.2.6 on 2023-11-25 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecomapp', '0008_products_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveBigIntegerField(default=1)),
                ('is_paid', models.BooleanField(default=False)),
                ('ProductsId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecomapp.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]