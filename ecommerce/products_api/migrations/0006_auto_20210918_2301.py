# Generated by Django 3.2.6 on 2021-09-18 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '0005_auto_20210918_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='unit_price',
            field=models.FloatField(default=0),
        ),
    ]
