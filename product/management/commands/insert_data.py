


















import requests
from django.core.management import BaseCommand
from product.models import Product, Category
from absl.testing.parameterized import product
from django.utils.text import slugify


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Creating data ......")
        response = requests.get('https://fakestoreapi.com/products').json();
        
        for product in response:
            category, _ = Category.objects.get_or_create(
                title = product['category'],
                slug = slugify(product['category'])
            )
            
            Product.objects.create(
                category = category,
                title = product['title'],
                slug = slugify(product['title']),
                price = product['price'],
                thumbnail = product['image'],
                description = product['description']
            )
        
        print("Data insert Complete ......")