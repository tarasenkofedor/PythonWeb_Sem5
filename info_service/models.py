from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
