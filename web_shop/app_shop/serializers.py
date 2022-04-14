from rest_framework import serializers
from app_shop.models import Product
from app_registration.models import Profile


class ProductSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=10000)
    price = serializers.IntegerField(default=0)
    created_at = serializers.DateField()

    def create(self, validated_data):
        """
        Создает и возвращает новый экземпляр 'Goods' с учетом проверки данных.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновляет и сохраняет значение экземпляра 'Goods', с учетом проверки данных
        """
        instance.authors = validated_data.get('author_id', instance.authors)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = "__all__"
