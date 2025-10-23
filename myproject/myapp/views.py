from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, 'myapp/home.html', {'items': items})

# def home(request):
#     items = Item.objects.all()
#     items_list = ", ".join([item.name for item in items])
#     return HttpResponse(f"Items: {items_list}")