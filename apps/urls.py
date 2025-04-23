from django.urls import path
from . import views

urlpatterns = [
    path('admin/login/', views.AdminLoginView.as_view(), name='admin-login'),

    # RestaurantPlace
    path('admin/places/', views.PlaceListCreateView.as_view(), name='place-list-create'),
    path('admin/places/<int:pk>/', views.PlaceRetrieveUpdateDestroyView.as_view(), name='place-detail'),

    # Dishes
    path('admin/dishes/', views.DishListCreateView.as_view(), name='dish-list-create'),
    path('admin/dishes/<int:pk>/', views.DishRetrieveUpdateDestroyView.as_view(), name='dish-detail'),
    path('reserve/', views.ReservationCreateView.as_view(), name='create-reservation'),
    path('admin/reservations/', views.AdminReservationListView.as_view(), name='admin-reservation-list'),
    path('admin/reservations/<int:pk>/confirm/', views.AdminReservationConfirmView.as_view(), name='admin-reservation-confirm'),
    path('admin/stats/top-dishes/', views.TopDishesView.as_view(), name='admin-top-dishes'),
    path('admin/stats/peak-times/', views.PeakTimesView.as_view(), name='admin-peak-times'),
]
