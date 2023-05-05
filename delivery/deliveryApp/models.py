from django.db import models


class DeliveryPoint(models.Model):
    class DeliveryType(models.IntegerChoices):
        SDEC = 1
        Yandex = 2
        home = 3

    delivery_type = models.IntegerField(choices=DeliveryType.choices)
    city = models.CharField(max_length=30, null=True, blank=True)
    X = models.FloatField(null=True, blank=True)
    Y = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)

    def __str__(self):
        if self.delivery_type == 1:
            return f'SDEC {self.lat} {self.lon}'
        elif self.delivery_type == 2:
            return f'Yandex {self.X} {self.Y}'
        else:
            return f'home {self.city}'
