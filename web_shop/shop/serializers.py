from rest_framework import serializers
from . import models


class GoodsSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=10000)
    price = serializers.IntegerField(default=0)
    created_at = serializers.DateField()

    def create(self, validated_data):
        """
        Создает и возвращает новый экземпляр 'Goods' с учетом проверки данных.
        """
        return models.Goods.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновляет и сохраняет значение экземпляра 'Goods', с учетом проверки данных
        """
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance


class ServicesSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=10000)
    price = serializers.IntegerField(default=0)
    created_at = serializers.DateField()

    def create(self, validated_data):
        """
        Создает и возвращает новый экземпляр`Service` с учетом проверенных данных.
        """
        return models.Service.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновляет и сохраняет значение экземпляра 'Service', с учетом проверки данных
        """
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance
