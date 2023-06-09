from django.urls import path
from .views import add_to_favorites, remove_from_favorites,my_favorites

urlpatterns = [
    path('favorites/', add_to_favorites, name='add_to_favorites'),
    path('favorites/<int:user_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('my_favorites/', my_favorites, name='my_favorites')
]