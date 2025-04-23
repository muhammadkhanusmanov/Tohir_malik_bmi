from django.contrib import admin
from .models import RestaurantPlace, Dish, Reservation, OrderItem


@admin.register(RestaurantPlace)
class RestaurantPlaceAdmin(admin.ModelAdmin):
    list_display = ("get_name_display", "capacity", "hourly_rate", "image_preview")
    list_filter = ("name",)
    search_fields = ("name", "description", "extra")

    def image_preview(self, obj):
        if obj.image:
            return f"<img src='{obj.image.url}' width='60' />"
        return "-"
    image_preview.allow_tags = True
    image_preview.short_description = "Rasm"

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "image_preview")
    list_filter = ("category",)
    search_fields = ("name", "description")

    def image_preview(self, obj):
        if obj.image:
            return f"<img src='{obj.image.url}' width='60' />"
        elif obj.image_url:
            return f"<img src='{obj.image_url}' width='60' />"
        return "-"
    image_preview.allow_tags = True
    image_preview.short_description = "Rasm"


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "place", "date", "start_time", "end_time", "is_confirmed", "get_place_price", "total_order_price", "full_total_price")
    list_filter = ("date", "is_confirmed")
    search_fields = ("full_name", "phone_number")
    readonly_fields = ("created_at",)

    def get_place_price(self, obj):
        return obj.get_place_price()
    get_place_price.short_description = "Joy narxi"

    def total_order_price(self, obj):
        return obj.total_order_price
    total_order_price.short_description = "Taomlar narxi"

    def full_total_price(self, obj):
        return obj.full_total_price
    full_total_price.short_description = "Umumiy narx"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("reservation", "dish", "quantity", "total_price")
    list_filter = ("dish",)
    search_fields = ("dish__name", "reservation__full_name")

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = "Narxi (x qty)"
