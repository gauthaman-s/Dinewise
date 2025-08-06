from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    session_key = models.CharField(max_length=40)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"

class Payment(models.Model):
    order_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    payment_time = models.DateTimeField(auto_now_add=True)
    receipt_url = models.URLField(blank=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
