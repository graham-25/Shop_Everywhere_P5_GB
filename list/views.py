from django.shortcuts import render
from .models import Item


# Create your views here.
def get_item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'list/item_list.html', context)