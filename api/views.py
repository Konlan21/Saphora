from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from store.models import *


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = 