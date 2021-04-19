from django.db import models


class Post(models.Model):
    description = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    medias = models.ManyToManyField('medias.Media')
    post_date = models.DateTimeField(auto_now_add=True)
