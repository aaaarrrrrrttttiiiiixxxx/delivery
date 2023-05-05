from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def get_delivery_points(self):
        pass

    @abstractmethod
    def get_delivery_cost(self, delivery_point):
        pass

    @abstractmethod
    def get_delivery_distance(self, delivery_point):
        pass