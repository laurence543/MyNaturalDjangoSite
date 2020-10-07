from django.db import models


# Класс модели  публикации новости
class Events(models.Model):
    title = models.CharField(max_length=100)
    annotation = models.CharField(max_length=256)
    content = models.CharField(max_length=1024)
    publish = models.DateTimeField()
    status = models.CharField(max_length=50)
