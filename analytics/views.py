from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import HistoricalPerformance
from .serializers import VendorPerformanceSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class VendorPerformanceViewset(viewsets.ViewSet):
    """
    API endpoint for retrieving vendor performance data.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def reterive(self, request, pk=None):
        """
        Retrieve historical performance data for a specific vendor.
        ---
        parameters:
            name: pk
            description: Vendor ID
            required: true
            type: integer
            paramType: path
        """
        try:
            queryset = HistoricalPerformance.objects.get(vendor_id=pk)
        except:
            return Response("Vendor Does not Exist.")
        serializer = VendorPerformanceSerializer(queryset)
        return Response(data=serializer.data)
