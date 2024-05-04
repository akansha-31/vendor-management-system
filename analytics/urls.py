from django.urls import path, include
from .views import VendorPerformanceViewset

urlpatterns = [
    path('vendors/<int:pk>/performance',
         VendorPerformanceViewset.as_view({'get': 'reterive'}), name='vendor-performance')
]
