from rest_framework import serializers
from .models import RestaurantPlace, Dish

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantPlace
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
        
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
