# Generated by Django 2.2 on 2022-03-10 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_goods_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsimages',
            old_name='goods',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='servicesimage',
            old_name='service',
            new_name='product',
        ),
    ]