# Generated by Django 3.2.6 on 2021-08-29 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.TextField(default='Pelotas', max_length=255),
        ),
    ]
