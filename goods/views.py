from django.shortcuts import get_list_or_404, get_object_or_404, render
from goods.models import Products
from django.core.paginator import Paginator

# Create your views here.
def catalog(request, category_slug):
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=category_slug))


    page = request.GET.get("page", 1)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": 'Home - Catalog',
        "goods": current_page,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product
    }

    return render(request, "goods/product.html", context)