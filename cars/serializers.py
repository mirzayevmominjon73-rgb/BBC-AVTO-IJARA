from rest_framework import serializers
from .models import Car, CarImage


class CarImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CarImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class CarSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = [
            'id',
            'title',
            'price',
            'category',
            'year',
            'color',
            'cpg',
            'images'
        ]

    def get_images(self, obj):
        request = self.context.get('request')

        # 1️⃣ Agar qo‘shimcha rasmlar bo‘lsa
        if obj.images.exists():
            return CarImageSerializer(
                obj.images.all(),
                many=True,
                context={'request': request}
            ).data

        # 2️⃣ Aks holda main_image ni beramiz
        if obj.main_image:
            return [{
                'id': 0,
                'image': request.build_absolute_uri(obj.main_image.url)
            }]

        return []
