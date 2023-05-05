from deliveryApp.deliveryServiceses.Delivery import Delivery
from deliveryApp.models import DeliveryPoint


class YandexDelivery(Delivery):
    def get_delivery_points(self):
        return DeliveryPoint.objects.filter(delivery_type=2)

    def get_delivery_cost(self, delivery_point):
        dist = self.get_delivery_distance(delivery_point)
        if dist < 10:
            return 200
        if dist < 100:
            return 1000
        return 2000


    def get_delivery_distance(self, delivery_point):
        return abs(delivery_point.X) + abs(delivery_point.Y)
