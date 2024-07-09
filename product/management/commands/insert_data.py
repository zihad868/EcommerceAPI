from typing import Any
from django.core.management import BaseCommand
from product.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        return super().handle(*args, **options)