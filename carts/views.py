from django.http import JsonResponse
from django.shortcuts import redirect, render
from goods.models import Products
from carts.models import Cart
from django.template.loader import render_to_string
from carts.utils import get_user_carts

def cart_add(request):

    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)


    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "message": "Product was succesfully added to cart",
        "cart_items_html": cart_items_html,
    }
    return JsonResponse(response_data)  #вернет на ту страницу с которой и положил предмет в карзину

def cart_change(request, product_slug):
    ...


def cart_remove(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])  #вернет на ту страницу с которой и положил предмет в карзину
