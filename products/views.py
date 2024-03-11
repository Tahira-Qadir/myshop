from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

from django.contrib import messages
from .forms import FeedbackForm
# Create your views here.
def home(request):
    products = Product.objects.all().order_by('id')[:4]  # Product models load
    return render(request, "products/home.html",{
        "products":products,
    })

def signup(request):
    return render(request, "products/signup.html")

def product_cat(request, product):
    if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("Does not exist.")

def product_page(request, product_brand, product_slug):
    product = Product.objects.get(slug = product_slug)
    form = FeedbackForm()
    if request.method == "GET":
        return render(request, "products/product.html", {
            "product": product,
            "form":form
            })
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            messages.success(request, "Your Feedback was submitted successfully.")
            form = FeedbackForm()
            
        return render(request, "products/product.html", {
            "product": product,
            "form":form
            })
    