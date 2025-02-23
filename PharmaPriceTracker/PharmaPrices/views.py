from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from django.shortcuts import render
from .models import Drug
from django.http import HttpResponse

def htmx_home(request):
    return render(request, 'htmx/htmx.html')

def drug_htmx_search(request):
    query = request.GET.get('search', '')
    drugs = Drug.objects.filter(name__icontains=query) | Drug.objects.filter(company__name__icontains=query)
    return render(request, 'htmx/drug_list.html', {'drugs': drugs})


def search_item(request):
    search_text = request.POST.get('search')
    results = Drug.objects.filter(name__icontains=search_text)
    context = {"results": results}
    return render(request, 'PharmaPrices/partials/search-results.html', context)

def clear(request):
    return HttpResponse("")



class CompanyListView(generic.ListView):
    model = models.Company
    form_class = forms.CompanyForm


class CompanyCreateView(generic.CreateView):
    model = models.Company
    form_class = forms.CompanyForm


class CompanyDetailView(generic.DetailView):
    model = models.Company
    form_class = forms.CompanyForm


class CompanyUpdateView(generic.UpdateView):
    model = models.Company
    form_class = forms.CompanyForm
    pk_url_kwarg = "pk"


class CompanyDeleteView(generic.DeleteView):
    model = models.Company
    success_url = reverse_lazy("PharmaPrices_Company_list")


class DataPointListView(generic.ListView):
    model = models.DataPoint
    form_class = forms.DataPointForm


class DataPointCreateView(generic.CreateView):
    model = models.DataPoint
    form_class = forms.DataPointForm


class DataPointDetailView(generic.DetailView):
    model = models.DataPoint
    form_class = forms.DataPointForm


class DataPointUpdateView(generic.UpdateView):
    model = models.DataPoint
    form_class = forms.DataPointForm
    pk_url_kwarg = "pk"


class DataPointDeleteView(generic.DeleteView):
    model = models.DataPoint
    success_url = reverse_lazy("PharmaPrices_DataPoint_list")


class DrugListView(generic.ListView):
    model = models.Drug
    form_class = forms.DrugForm


class DrugCreateView(generic.CreateView):
    model = models.Drug
    form_class = forms.DrugForm


class DrugDetailView(generic.DetailView):
    model = models.Drug
    form_class = forms.DrugForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datapoints'] = models.DataPoint.objects.filter(drug=self.object).order_by('date')
        return context



class DrugUpdateView(generic.UpdateView):
    model = models.Drug
    form_class = forms.DrugForm
    pk_url_kwarg = "pk"


class DrugDeleteView(generic.DeleteView):
    model = models.Drug
    success_url = reverse_lazy("PharmaPrices_Drug_list")