from django.db import models
from django.conf import settings


class Post(models.Model):
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medias = models.ManyToManyField('medias.Media')
    post_date = models.DateTimeField(auto_now_add=True)
