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
from .models import RestaurantPlace, Dish,Reservation,OrderItem
from .serialazers import PlaceSerializer, DishSerializer, ReservationSerializer

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


from datetime import datetime
from django.db.models import Q

class ReservationCreateView(APIView):
    permission_classes = [permissions.AllowAny]  # Barcha foydalanuvchilar uchun ochiq
    def post(self, request):
        data = request.data.copy()
        order_items_data = data.pop('order_items', [])

        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            place_id = serializer.validated_data['place'].id
            date = serializer.validated_data['date']
            start_time = serializer.validated_data['start_time']
            end_time = serializer.validated_data['end_time']

            # Bandlikni tekshirish
            conflicts = Reservation.objects.filter(
                place_id=place_id,
                date=date,
                start_time__lt=end_time,
                end_time__gt=start_time
            )
            if conflicts.exists():
                return Response(
                    {"error": "Bu vaqtda bu joy allaqachon band qilingan."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Saqlash
            reservation = serializer.save()

            # Taom buyurtmalarini qo‘shish
            for item in order_items_data:
                try:
                    dish = Dish.objects.get(id=item['dish'])
                    quantity = int(item['quantity'])
                    OrderItem.objects.create(reservation=reservation, dish=dish, quantity=quantity)
                except Dish.DoesNotExist:
                    continue

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AdminReservationListView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        reservations = Reservation.objects.all().order_by('-created_at')
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class AdminReservationConfirmView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, pk):
        try:
            reservation = Reservation.objects.get(id=pk)
            reservation.is_confirmed = True
            reservation.save()
            return Response({"message": "Buyurtma tasdiqlandi."})
        except Reservation.DoesNotExist:
            return Response({"error": "Buyurtma topilmadi."}, status=status.HTTP_404_NOT_FOUND)

class TopDishesView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        top_dishes = (
            OrderItem.objects.values('dish__name')
            .annotate(total_sold=Sum('quantity'))
            .order_by('-total_sold')[:5]
        )
        return Response(top_dishes)

class PeakTimesView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        peak_times = (
            Reservation.objects.values('start_time')
            .annotate(count=Count('id'))
            .order_by('-count')[:5]
        )
        return Response(peak_times)