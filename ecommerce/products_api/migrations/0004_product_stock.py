# Generated by Django 3.2.6 on 2021-09-13 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '0003_alter_product_unitprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]