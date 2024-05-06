from rest_framework import viewsets
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class VendorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing vendors.
    ---
    description: This endpoint allows you to perform CRUD operations on vendors.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
