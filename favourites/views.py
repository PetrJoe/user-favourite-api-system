from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Favorite
from .serializers import FavoriteSerializer
from accounts.serializers import UserSerializer
from django.conf import settings
from django.contrib.auth import get_user_model

User = settings.AUTH_USER_MODEL


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_favorites(request):
    serializer = FavoriteSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({'status': 'success', 'message': 'User added to favorites successfully'})
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_favorites(request, user_id):
    User = get_user_model()
    user_to_remove = User.objects.get(id=user_id)
    Favorite.objects.filter(user=request.user, favorite_user=user_to_remove).delete()
    return Response({'status': 'success', 'message': 'User removed from favorites'})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_favorites(request):
    my_id = request.user.id
    User = get_user_model()
    favorites = User.objects.filter(favorite_of__user_id=my_id)
    serializer = UserSerializer(favorites, many=True)
    return Response(serializer.data)