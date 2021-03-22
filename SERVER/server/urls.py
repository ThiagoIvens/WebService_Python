from django.urls import path
from . import views

urlpatterns = [
    path('weather-list/', views.weatherList, name='weather_list'),
    path('weather-detail/<str:pk>/', views.weatherDetail, name='weather_detail'),
    path('weather-detail-time/<str:hora>/', views.weatherDetailH, name='weather_detail_time'),
    path('weather-create/', views.weatherCreate, name='weather_create'),
    path('weather-update/<str:pk>/', views.weatherUpdate, name='weather_update'),
    path('weather-delete/<str:pk>/', views.weatherDelete, name='weather_delete'),
]