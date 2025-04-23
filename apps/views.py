from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class AdminLoginView(APIView):
    authentication_classes = [BasicAuthentication]
    def post(self, request):
        user = request.user

        if user and user.is_staff:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Noto‘g‘ri login yoki parol"}, status=status.HTTP_401_UNAUTHORIZED)

from rest_framework import generics, permissions
from .models import RestaurantPlace, Dish
from .serialazers import PlaceSerializer, DishSerializer

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


# RestaurantPlace Viewlar
class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = RestaurantPlace.objects.all()
    serializer_class = PlaceSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]  # hammaga ochiq
        return [IsAdminUser()]

class PlaceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantPlace.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAdminUser]


# Dish Viewlar
class DishListCreateView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]  # hammaga ochiq
        return [IsAdminUser()]

class DishRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminUser]
