from rest_framework import serializers
from .models import Favorite
from django.contrib.auth.models import User

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'favorite_user']
        read_only_fields = ['created_at']

    def validate(self, data):
        user_to_add = data['favorite_user']
        adding_user = self.context['request'].user
        if user_to_add == adding_user:
            raise serializers.ValidationError("You cannot add yourself to favorites")
        if Favorite.objects.filter(user=adding_user, favorite_user=user_to_add).exists():
            raise serializers.ValidationError("This user is already in your favorites")
        return data