from django.db import models


# Класс модели  публикации новости
class Posts(models.Model):
    title = models.CharField(max_length=100)
    annotation = models.CharField(max_length=256)
    content = models.CharField(max_length=1024)
    link = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    publish = models.DateTimeField()
    status = models.CharField(max_length=50)
