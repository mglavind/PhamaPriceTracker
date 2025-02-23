from rest_framework import viewsets, permissions

from . import serializers
from . import models


class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class"""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class DataPointViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataPoint class"""

    queryset = models.DataPoint.objects.all()
    serializer_class = serializers.DataPointSerializer
    permission_classes = [permissions.IsAuthenticated]


class DrugViewSet(viewsets.ModelViewSet):
    """ViewSet for the Drug class"""

    queryset = models.Drug.objects.all()
    serializer_class = serializers.DrugSerializer
    permission_classes = [permissions.IsAuthenticated]