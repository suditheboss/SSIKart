from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.
def home(request):
     products = Product.objects.filter(is_available=True)
     context_data = {
        "products":products,
     }
     return render(request, 'home/home.html',  context_data)

def about(request):
    return render(request, 'home/about.html')

def checkout(request):
    return render(request, 'home/checkout.html')