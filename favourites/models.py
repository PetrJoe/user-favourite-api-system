from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_user = models.ForeignKey(User, related_name='favorite_of', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'favorite_user')

    def __str__(self):
        return f'{self.user.email} added {self.favorite_user.email} to favorites'
