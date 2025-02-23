from django.db import models
from django.urls import reverse


class Company(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=100)
    website = models.URLField()
    description = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("PharmaPrices_Company_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PharmaPrices_Company_update", args=(self.pk,))



class DataPoint(models.Model):

    # Relationships
    drug = models.ForeignKey("PharmaPrices.Drug", on_delete=models.CASCADE)

    # Fields
    price = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PharmaPrices_DataPoint_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PharmaPrices_DataPoint_update", args=(self.pk,))



class Drug(models.Model):

    # Relationships
    company = models.ForeignKey("PharmaPrices.Company", on_delete=models.CASCADE)

    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    website = models.URLField()

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("PharmaPrices_Drug_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PharmaPrices_Drug_update", args=(self.pk,))