# Generated by Django 3.2.6 on 2021-09-12 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '0002_alter_product_category'),
        ('carts_api', '0002_auto_20210905_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_api.product'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='subTotal',
            field=models.FloatField(default=0),
        ),
    ]