from django.db import models
from datetime import datetime, timedelta

class RestaurantPlace(models.Model):
    PLACE_TYPE_CHOICES = [
        ('vip', 'VIP'),
        ('private', 'Alohidalik'),
        ('family', 'Oilaviy'),
        ('standard', 'Standart'),
    ]

    name = models.CharField(max_length=100, choices=PLACE_TYPE_CHOICES)
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="Rasm URL manzili (ixtiyoriy)")
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # Har soat uchun narx

    def __str__(self):
        return f"{self.get_name_display()} ({self.capacity} kishi)"


class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('drink', 'Ichimlik'),
        ('soup', 'Suyuq ovqat'),
        ('salat', 'Salat'),
        ('main', 'Asosiy taom'),
        ('dessert', 'Shirinlik'),
        ('other', 'Boshqa'),
    ]

    name = models.CharField(max_length=35)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="Rasm URL manzili (ixtiyoriy)")


    def __str__(self):
        return f"{self.name} - {self.price} so'm"

class Reservation(models.Model):
    place = models.ForeignKey(RestaurantPlace, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def duration_hours(self):
        delta = datetime.combine(self.date, self.end_time) - datetime.combine(self.date, self.start_time)
        return max(delta.total_seconds() // 3600, 1)  # kamida 1 soat

    @property
    def total_order_price(self):
        return sum(item.total_price for item in self.order_items.all())
    
    @property
    def full_total_price(self):
        return self.get_place_price() + self.total_order_price
    
    def get_total_price(self):
        hours = self.duration_hours()
        extra_hours = max(hours - 1, 0)
        return extra_hours * self.place.hourly_rate

    def __str__(self):
        return f"{self.full_name} ({self.date} {self.start_time}-{self.end_time})"


class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='order_items')
    
    @property
    def total_price(self):
        return self.quantity * self.dish.price

    def __str__(self):
        return f"{self.quantity} x {self.dish.name}"
