from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    products = Product.objects.all().order_by('id')[:4]  # Product models load
    return render(request, "products/home.html",{
        "products":products,
    })

def signup(request):
    return render(request, "products/signup.html")

def product_cat(requeste, product):
    if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("Does not exist.")