# Generated by Django 5.1.2 on 2024-10-27 19:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(related_name='wishlists', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]