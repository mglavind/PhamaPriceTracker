from rest_framework import serializers

from . import models


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = [
            "last_updated",
            "created",
            "name",
            "website",
            "description",
        ]

class DataPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DataPoint
        fields = [
            "price",
            "last_updated",
            "date",
            "created",
            "drug",
        ]

class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Drug
        fields = [
            "name",
            "created",
            "description",
            "last_updated",
            "website",
            "company",
        ]