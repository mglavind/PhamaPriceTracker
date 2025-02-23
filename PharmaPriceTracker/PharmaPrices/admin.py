from django.contrib import admin
from django import forms

from . import models


class CompanyAdminForm(forms.ModelForm):

    class Meta:
        model = models.Company
        fields = "__all__"


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyAdminForm
    list_display = [
        "last_updated",
        "created",
        "name",
        "website",
        "description",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class DataPointAdminForm(forms.ModelForm):

    class Meta:
        model = models.DataPoint
        fields = "__all__"


class DataPointAdmin(admin.ModelAdmin):
    form = DataPointAdminForm
    list_display = [
        "price",
        "last_updated",
        "date",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class DrugAdminForm(forms.ModelForm):

    class Meta:
        model = models.Drug
        fields = "__all__"


class DrugAdmin(admin.ModelAdmin):
    form = DrugAdminForm
    list_display = [
        "name",
        "created",
        "description",
        "last_updated",
        "website",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.DataPoint, DataPointAdmin)
admin.site.register(models.Drug, DrugAdmin)