from django.urls import path
from .views import (
    home,
    product_cat,
    signup
)

urlpatterns = [
    path('', home, name='Home'),
    path('products/<product>', product_cat, name='pro_cat'), # <> show the Dynamic URLs
    path('signup/', signup, name='Signup'), # Signup Page
]