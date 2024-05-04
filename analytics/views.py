from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import HistoricalPerformance
from .serializers import VendorPerformanceSerializer

# Create your views here.


class VendorPerformanceViewset(viewsets.ViewSet):

    def reterive(self, request, pk=None):
        queryset = HistoricalPerformance.objects.get(vendor_id=pk)
        serializer = VendorPerformanceSerializer(queryset)
        return Response(data=serializer.data)
