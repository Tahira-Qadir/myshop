from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Feedback

from django.views import View
from django.contrib import messages
from .forms import FeedbackForm
# Create your views here.

class IndexView(View):
    def get(self, request):
        products = Product.objects.all().order_by('id')[:4]  # Product models load
        return render(request, "products/home.html",{
            "products":products,
        })
    def post(self, request):
        pass

class ProductPageView(View):
    def get(self, request, product_brand, product_slug):
        product = Product.objects.get(slug = product_slug)
        my_feedback = Feedback.objects.get(product=product, id =1)
        form = FeedbackForm(instance=my_feedback)
        reviews = Feedback.objects.filter(product = product)
        return render(request, "products/product.html", {
            "product": product,
            "form":form,
            "reviews": reviews,
            })
    def post(self, request, product_brand, product_slug):
        product = Product.objects.get(slug = product_slug)
        my_feedback = Feedback.objects.get(product=product, id =1)
        form = FeedbackForm(request.POST, instance=my_feedback)
        reviews = Feedback.objects.filter(product = product)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Feedback was submitted successfully.")

        return render(request, "products/product.html", {
            "product": product,
            "form":form,
            "reviews": reviews,
            })
def signup(request):
    return render(request, "products/signup.html")

def product_cat(request, product):
    if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("Does not exist.")

        
    