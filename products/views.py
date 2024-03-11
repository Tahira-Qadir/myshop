from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Feedback

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
    my_feedback = Feedback.objects.get(product=product, id =1)
    form = FeedbackForm(instance=my_feedback)
    reviews = Feedback.objects.filter(product = product)
    if request.method == "GET":
        return render(request, "products/product.html", {
            "product": product,
            "form":form,
            "reviews": reviews,
            })
    else:
        form = FeedbackForm(request.POST, instance=my_feedback)
        if form.is_valid():
            form.save()
            # feedback = Feedback(
            #     name = form.cleaned_data["name"],
            #     rating = form.cleaned_data["rating"],
            #     product = product,
            #     text = form.cleaned_data["text"]
            # )
            # feedback.save()
            messages.success(request, "Your Feedback was submitted successfully.")
            # form = FeedbackForm()

        return render(request, "products/product.html", {
            "product": product,
            "form":form,
            # "reviews": reviews,
            })
    