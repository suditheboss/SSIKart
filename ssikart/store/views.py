from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import category

# Create your views here.
def store_home(request):
     products = Product.objects.filter(is_available=True)
     products_count = products.count()
     context_data = {
        "products":products,
        "products_count":products_count
     }
     return render(request,"store/product_details.html",context_data)

def shop(request,category_slug=None):
      categories = None
      products = None

      if category_slug != None:
       categories = get_object_or_404(category, slug=category_slug)
       products = Product.objects.all().filter(category= categories, is_available=True)
       products_count = products.count()
      else:
       products = Product.objects.all().filter(is_available=True)
      products_count = products.count()
       
      context_data = {
        "products":products,
        "products_count":products_count
       }
      return render(request,"store/shop.html",context_data)
