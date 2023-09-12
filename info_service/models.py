from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from repair_service.models import Service


class News(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='info_service/news',
                              help_text='News image',
                              blank=True,
                              null=True)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PromoCode(models.Model):
    code = models.IntegerField(unique=True)
    expiration_date = models.DateField()
    discount = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.code}-{self.expiration_date}'


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=50)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    reviewer_name = models.CharField(max_length=30)
    used_service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    text = models.TextField(max_length=256)
    score = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.reviewer_name}-{self.score}'
