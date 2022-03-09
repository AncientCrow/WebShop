# Generated by Django 2.2 on 2022-03-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_service_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='description_en',
            field=models.TextField(max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='goods',
            name='description_ru',
            field=models.TextField(max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='goods',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='goods',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
    ]