from django.urls import path
from Dinewise_app.views import (
    Index, Login, Register, Cart, PaymentGateway, Receipt,
    Restaurant1, Restaurant2, Restaurant3, Restaurant4
)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('cart/', Cart.as_view(), name='cart'),
    path('payment/', PaymentGateway.as_view(), name='payment_gateway'),
    path('receipt/', Receipt.as_view(), name='receipt'),
    path('restaurant-1/', Restaurant1.as_view(), name='restaurant_1'),
    path('restaurant-2/', Restaurant2.as_view(), name='restaurant_2'),
    path('restaurant-3/', Restaurant3.as_view(), name='restaurant_3'),
    path('restaurant-4/', Restaurant4.as_view(), name='restaurant_4'),
]