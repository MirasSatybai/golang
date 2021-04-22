from django.contrib import admin
from .models import *
from posts import models.Post as Post
from medias import models.Media as Media

admin.site.register(User)
admin.site.register(Media)
admin.site.register(Post)

