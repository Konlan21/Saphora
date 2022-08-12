from django.forms import DecimalField
from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from django.db.models import F, Value, Func
from django.db.models.functions import Concat
from django.http import HttpResponse
from store.models import Product, Customer


def say_hello(request):
    return HttpResponse('Hello World')
