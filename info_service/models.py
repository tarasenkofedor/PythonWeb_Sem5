from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

from account.models import Account
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
    reviewer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    used_service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )
    text = models.TextField(max_length=256)
    score = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.reviewer.email}-{self.score}'


class Worker(models.Model):
    name = models.CharField(max_length=256)
    age = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    job_title = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')]
    )
    email = models.EmailField(unique=True)
    image = models.ImageField(
        upload_to='info_service/workers',
        help_text='Worker image',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
