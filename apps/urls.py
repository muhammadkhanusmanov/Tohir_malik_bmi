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
]
