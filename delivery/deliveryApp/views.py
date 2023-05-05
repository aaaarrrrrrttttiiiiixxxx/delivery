from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from deliveryApp.Serializers import DeliveryPointSerializer, CostSerializer
from deliveryApp.Serializers import PointIdSerializer
from deliveryApp.deliveryServiceses.SDECDelivery import SDECDelivery
from deliveryApp.models import DeliveryPoint
from deliveryApp.deliveryServiceses.HomeDelivery import HomeDelivery
from deliveryApp.deliveryServiceses.YandexDelivery import YandexDelivery


class SDECView(APIView):
    @swagger_auto_schema(
        operation_summary="Получение списка всех точек для СДЕК",
        responses={200: DeliveryPointSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request):
        service = SDECDelivery()
        points = service.get_delivery_points()
        serializer = DeliveryPointSerializer(points, many=True)
        return JsonResponse(serializer.data, safe=False)


class YandexView(APIView):
    @swagger_auto_schema(
        operation_summary="Получение списка всех точек для Яндекс",
        responses={200: DeliveryPointSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request):
        service = YandexDelivery()
        points = service.get_delivery_points()
        serializer = DeliveryPointSerializer(points, many=True)
        return JsonResponse(serializer.data, safe=False)


class HomeView(APIView):
    @swagger_auto_schema(
        operation_summary="Получение списка всех точек для доставки до дома",
        responses={200: DeliveryPointSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request):
        service = HomeDelivery()
        points = service.get_delivery_points()
        serializer = DeliveryPointSerializer(points, many=True)
        return JsonResponse(serializer.data, safe=False)


class GetCost(APIView):
    @swagger_auto_schema(
        operation_summary="получение стоимости доставки до точки",
        responses={200: CostSerializer(many=False), 500: "Серверная ошибка"},
        request_body=PointIdSerializer
    )
    def post(self, request):
        request_serializer = PointIdSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        point = get_object_or_404(DeliveryPoint, pk=request_serializer.validated_data['id'])
        if point.delivery_type == 1:
            service = SDECDelivery()
        elif point.delivery_type == 2:
            service = YandexDelivery()
        else:
            service = HomeDelivery()
        cost = service.get_delivery_cost(point)
        serializer = CostSerializer({'cost': cost})
        return JsonResponse(serializer.data, safe=False)
