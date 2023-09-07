from django.db import models


class ServiceTag(models.Model):
    name = models.CharField(max_length=64,
                            help_text='Tag of service',
                            primary_key=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=128,
                            unique=True,
                            help_text='Name of service')

    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                help_text='Cost of service')

    about = models.CharField(max_length=256,
                             default='Empty description',
                             help_text='Full description of service')

    service_tags = models.ManyToManyField(ServiceTag)
    image = models.ImageField(upload_to='service_images/',
                              help_text='Service image',
                              blank=True,
                              null=True)

    def __str__(self):
        return self.name
