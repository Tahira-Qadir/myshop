from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    user = "Tahira"
    product_numb = 4
    return render(request, "products/home.html",{
        "name":user,
        "product_numb":product_numb,
    })

def signup(request):
    return render(request, "products/signup.html")

def product_cat(requeste, product):
    if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("Does not exist.")