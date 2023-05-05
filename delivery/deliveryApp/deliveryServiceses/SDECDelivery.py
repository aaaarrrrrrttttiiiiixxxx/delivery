from math import sqrt, cos, sin, atan2

from deliveryApp.models import DeliveryPoint

from deliveryApp.deliveryServiceses.Delivery import Delivery


class SDECDelivery(Delivery):
    def get_delivery_points(self):
        return DeliveryPoint.objects.filter(delivery_type=1)

    def get_delivery_cost(self, delivery_point):
        dist = self.get_delivery_distance(delivery_point)
        if dist < 100:
            return 1000
        if dist > 1000:
            return 1000
        return round(dist)

    def get_delivery_distance(self, delivery_point):
        R = 6371
        dLat = (delivery_point.lat - 0) * (3.14/180)
        dLon = (delivery_point.lon - 0) * (3.14/180)
        a = sin(dLat / 2) * sin(dLat / 2) + cos(0) * cos(delivery_point.lat * (3.14/180)) * sin(dLon / 2) * sin(dLon / 2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c

