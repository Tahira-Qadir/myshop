from django.urls import path
from .views import (
    IndexView,
    signup,
    ProductPageView,
    product_cat,
)

urlpatterns = [
    path('', IndexView.as_view(), name='Home'),
    path('products/<product>', product_cat, name='pro_cat'), # <> show the Dynamic URLs
    path('signup/', signup, name='Signup'), # Signup Page
    path('products/<product_brand>/<product_slug>', ProductPageView.as_view(), name='product_page'), # Single Product View
]