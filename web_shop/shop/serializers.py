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
        Create and return a new `Snippet` instance, given the validated data.
        """
        return models.Goods.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
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
        Create and return a new `Snippet` instance, given the validated data.
        """
        return models.Service.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
