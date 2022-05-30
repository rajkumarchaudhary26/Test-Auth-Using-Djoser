from django.shortcuts import render
from .models import Product
from django.db.models import F
# Create your views here.
def home(request):
    product = Product.objects.get(pk = 1)
    # print(product)
    # print(type(product))
    # print(product.name)
    print(type(product.quantity))
    print(type(F(product.quantity)))
    context = {
        'product':product,
    }
    return render(request, 'index.html', context)
