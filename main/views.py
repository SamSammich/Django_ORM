from django.shortcuts import render

from main.models import Product


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'PandaShop'
    }

    return render(request, 'main/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
    context = {
        'title': 'Contact'
    }

    return render(request, 'main/contact.html', context)
