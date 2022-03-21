# Generated by Django 2.2 on 2022-03-18 07:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='title')),
                ('description', models.TextField(max_length=10000, verbose_name='description')),
                ('description_ru', models.TextField(max_length=10000, null=True, verbose_name='description')),
                ('description_en', models.TextField(max_length=10000, null=True, verbose_name='description')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('created_at', models.DateField(default=datetime.datetime(2022, 3, 18, 7, 57, 48, 149998, tzinfo=utc), editable=False, verbose_name='created date')),
                ('status', models.CharField(choices=[('m', 'У модерации'), ('a', 'Активное'), ('i', 'Неактивное')], default='d', max_length=1, verbose_name='status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'db_table': 'goods',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='title')),
                ('description', models.TextField(max_length=10000, verbose_name='description')),
                ('description_ru', models.TextField(max_length=10000, null=True, verbose_name='description')),
                ('description_en', models.TextField(max_length=10000, null=True, verbose_name='description')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('created_at', models.DateField(default=datetime.datetime(2022, 3, 18, 7, 57, 48, 149250, tzinfo=utc), editable=False, verbose_name='created date')),
                ('status', models.CharField(choices=[('m', 'У модерации'), ('a', 'Активное'), ('i', 'Неактивное')], default='d', max_length=1, verbose_name='status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'db_table': 'services',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ServicesImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='services/%Y_%m_%d', verbose_name='image')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_images', to='shop.Service')),
            ],
            options={
                'db_table': 'service_files',
            },
        ),
        migrations.CreateModel(
            name='GoodsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='goods/%Y_%m_%d', verbose_name='image')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goods_images', to='shop.Goods')),
            ],
            options={
                'db_table': 'goods_files',
            },
        ),
    ]
