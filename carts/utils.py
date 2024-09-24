
from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    
    if not request.session.session_key:         # чтобы незарег пользователь мог добавлять элементы в корзину, создаем ему session_key
        request.session.create()

    return Cart.objects.filter(session_key=request.session.session_key)      # показываем ему элементы с корзины по session_key, а не request.user
    