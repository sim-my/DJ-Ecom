from django.urls import path
from .views import products, checkout, home

app_name = 'core'

urlpatterns = [
    path('products/', products, name="products"),
    path('checkout/', checkout, name="checkout"),
    path('', home, name="home"),

]
