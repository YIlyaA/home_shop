from django.shortcuts import render
from goods.models import Categories, Products

# Create your views here.
def catalog(request):
    goods = Products.objects.all()

    context = {
        "title": 'Home - Catalog',
        "goods": goods,
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    pass