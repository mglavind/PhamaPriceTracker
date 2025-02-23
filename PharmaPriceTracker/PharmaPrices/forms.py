from django import forms
from PharmaPrices.models import Drug
from PharmaPrices.models import Company
from . import models


class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = [
            "name",
            "website",
            "description",
        ]


class DataPointForm(forms.ModelForm):
    class Meta:
        model = models.DataPoint
        fields = [
            "price",
            "date",
            "drug",
        ]

    def __init__(self, *args, **kwargs):
        super(DataPointForm, self).__init__(*args, **kwargs)
        self.fields["drug"].queryset = Drug.objects.all()



class DrugForm(forms.ModelForm):
    class Meta:
        model = models.Drug
        fields = [
            "name",
            "description",
            "website",
            "company",
        ]

    def __init__(self, *args, **kwargs):
        super(DrugForm, self).__init__(*args, **kwargs)
        self.fields["company"].queryset = Company.objects.all()