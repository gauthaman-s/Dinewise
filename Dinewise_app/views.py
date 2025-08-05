from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

class Cart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cart.html')

class PaymentGateway(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'payment gateway.html')

class Receipt(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'receipt.html')

class Restaurant1(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant-1.html')

class Restaurant2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant-2.html')

class Restaurant3(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant-3.html')

class Restaurant4(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant-4.html')