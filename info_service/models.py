from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='info_service/news',
                              help_text='News image',
                              blank=True,
                              null=True)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
