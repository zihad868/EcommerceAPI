from rest_framework import serializers


from . models import (
    Product, 
    Category
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['category'] = {'id': instance.category.id, 'title': instance.category.title, 'slug': instance.category.slug}
        return context   