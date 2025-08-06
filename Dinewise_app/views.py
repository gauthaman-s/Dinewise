from django.shortcuts import render, redirect
from django.views import View
from .models import Payment, User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
import uuid

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists.'})
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        request.session['user_id'] = user.id
        return redirect('index')

class Cart(View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', [])
        total = sum(int(item['price']) * int(item.get('quantity', 1)) for item in cart)
        return render(request, 'cart.html', {'cart': cart, 'total': total})

    def post(self, request, *args, **kwargs):
        cart = request.session.get('cart', [])
        # Handle delete item
        if 'delete_index' in request.POST:
            delete_index = int(request.POST['delete_index'])
            if 0 <= delete_index < len(cart):
                cart.pop(delete_index)
                request.session['cart'] = cart
        # Handle clear cart
        if 'clear_cart' in request.POST:
            cart = []
            request.session['cart'] = cart
        total = sum(int(item['price']) * int(item.get('quantity', 1)) for item in cart)
        return render(request, 'cart.html', {'cart': cart, 'total': total})

class PaymentGateway(View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', [])
        total = sum(int(item['price']) * int(item.get('quantity', 1)) for item in cart)
        return render(request, 'payment gateway.html', {'cart': cart, 'total': total})

    def post(self, request, *args, **kwargs):
        cart = request.session.get('cart', [])
        total = sum(int(item['price']) * int(item.get('quantity', 1)) for item in cart)
        # Simulate Gokwik payment integration
        order_id = str(uuid.uuid4())
        # Here you would call Gokwik API and get payment status/receipt
        # For demo, we assume payment is successful
        payment = Payment.objects.create(
            order_id=order_id,
            amount=total,
            status='Success',
            details=str(cart),
            receipt_url='' # Could be a generated PDF or link
        )
        request.session['cart'] = []
        request.session['last_payment_id'] = payment.id
        return redirect('receipt')

class Receipt(View):
    def get(self, request, *args, **kwargs):
        payment_id = request.session.get('last_payment_id')
        payment = Payment.objects.filter(id=payment_id).first()
        return render(request, 'receipt.html', {'payment': payment})

class Restaurant1(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant-1.html')

    def post(self, request, *args, **kwargs):
        item = {
            'name': request.POST.get('item_name'),
            'price': request.POST.get('item_price'),
            'image': request.POST.get('item_image'),
            'quantity': request.POST.get('item_quantity', 1),
            'restaurant': 'restaurant_1',
        }
        cart = request.session.get('cart', [])
        # Only allow items from the same restaurant
        if cart and any(i['restaurant'] != 'restaurant_1' for i in cart):
            return render(request, 'restaurant-1.html', {'error': 'You can only order items from the same restaurant. Please clear your cart first.'})
        cart.append(item)
        request.session['cart'] = cart
        return redirect('restaurant_1')

class Restaurant2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant-2.html')

    def post(self, request, *args, **kwargs):
        item = {
            'name': request.POST.get('item_name'),
            'price': request.POST.get('item_price'),
            'image': request.POST.get('item_image'),
            'quantity': request.POST.get('item_quantity', 1),
            'restaurant': 'restaurant_2',
        }
        cart = request.session.get('cart', [])
        if cart and any(i['restaurant'] != 'restaurant_2' for i in cart):
            return render(request, 'restaurant-2.html', {'error': 'You can only order items from the same restaurant. Please clear your cart first.'})
        cart.append(item)
        request.session['cart'] = cart
        return redirect('restaurant_2')

class Restaurant3(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant-3.html')

    def post(self, request, *args, **kwargs):
        item = {
            'name': request.POST.get('item_name'),
            'price': request.POST.get('item_price'),
            'image': request.POST.get('item_image'),
            'quantity': request.POST.get('item_quantity', 1),
            'restaurant': 'restaurant_3',
        }
        cart = request.session.get('cart', [])
        if cart and any(i['restaurant'] != 'restaurant_3' for i in cart):
            return render(request, 'restaurant-3.html', {'error': 'You can only order items from the same restaurant. Please clear your cart first.'})
        cart.append(item)
        request.session['cart'] = cart
        return redirect('restaurant_3')

class Restaurant4(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant-4.html')

    def post(self, request, *args, **kwargs):
        item = {
            'name': request.POST.get('item_name'),
            'price': request.POST.get('item_price'),
            'image': request.POST.get('item_image'),
            'quantity': request.POST.get('item_quantity', 1),
            'restaurant': 'restaurant_4',
        }
        cart = request.session.get('cart', [])
        if cart and any(i['restaurant'] != 'restaurant_4' for i in cart):
            return render(request, 'restaurant-4.html', {'error': 'You can only order items from the same restaurant. Please clear your cart first.'})
        cart.append(item)
        request.session['cart'] = cart
        return redirect('restaurant_4')