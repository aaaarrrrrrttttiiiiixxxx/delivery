from rest_framework import serializers

from deliveryApp.models import DeliveryPoint


class DeliveryPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPoint
        fields = '__all__'


# class SDECPointSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeliveryPoint
#         fields = ['id', 'lon', 'lat']
#
#
# class YandexPointSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeliveryPoint
#         fields = ['id', 'X', 'Y']
#
#
# class HomePointSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeliveryPoint
#         fields = ['id', 'city']

# class PointIdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeliveryPoint
#         fields = ['id']

class PointIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class CostSerializer(serializers.Serializer):
    cost = serializers.IntegerField()
