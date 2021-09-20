from django.shortcuts import render
from API.main import get_orders
from django.http import HttpResponse

def index(request):
    return HttpResponse(get_orders.response().keys())

