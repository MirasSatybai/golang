from django.db import models


class Media(models.Model):
    name = models.CharField(max_length=255)
    url = models.TextField()
    file = models.FileField(upload_to='media/')
