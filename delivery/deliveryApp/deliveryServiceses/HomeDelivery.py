from deliveryApp.deliveryServiceses.Delivery import Delivery
from deliveryApp.models import DeliveryPoint


class HomeDelivery(Delivery):
    def get_delivery_points(self):
        return DeliveryPoint.objects.filter(delivery_type=3)

    def get_delivery_cost(self, delivery_point):
        # if delivery_point.city == 'Moscow' or delivery_point.city == "Saint Petersburg":
        #     return True, 700
        # return False, -1
        return 700

    def get_delivery_distance(self, delivery_point):
        pass