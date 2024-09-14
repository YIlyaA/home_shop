from django.shortcuts import render
from goods.models import Categories

# Create your views here.
def index(request):

    context = {
        "title": "HOME Furniture Store"
    }
    return render(request, "main/index.html", context)


def about(request):

    return render(request, "main/about.html")