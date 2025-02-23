from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import HttpResponse
from django.views import generic
from django.template import Template, RequestContext
from django.template.response import TemplateResponse

from . import models
from . import forms


class HTMXCompanyListView(generic.ListView):
    model = models.Company
    form_class = forms.CompanyForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request,'htmx/list.html', context)


class HTMXCompanyCreateView(generic.CreateView):
    model = models.Company
    form_class = forms.CompanyForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(request, 'htmx/form.html', context)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "object": self.object,
            "form": form
        }
        return TemplateResponse(self.request, 'htmx/create.html', context)

    def form_invalid(self, form):
        super().form_invalid(form)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(self.request, 'htmx/form.html', context)


class HTMXCompanyDeleteView(generic.DeleteView):
    model = models.Company
    success_url = reverse_lazy("PharmaPrices_Company_htmx_list")
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()


class HTMXDataPointListView(generic.ListView):
    model = models.DataPoint
    form_class = forms.DataPointForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request,'htmx/list.html', context)


class HTMXDataPointCreateView(generic.CreateView):
    model = models.DataPoint
    form_class = forms.DataPointForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(request, 'htmx/form.html', context)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "object": self.object,
            "form": form
        }
        return TemplateResponse(self.request, 'htmx/create.html', context)

    def form_invalid(self, form):
        super().form_invalid(form)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(self.request, 'htmx/form.html', context)


class HTMXDataPointDeleteView(generic.DeleteView):
    model = models.DataPoint
    success_url = reverse_lazy("PharmaPrices_DataPoint_htmx_list")
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()


class HTMXDrugListView(generic.ListView):
    model = models.Drug
    form_class = forms.DrugForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request,'htmx/list.html', context)


class HTMXDrugCreateView(generic.CreateView):
    model = models.Drug
    form_class = forms.DrugForm
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(request, 'htmx/form.html', context)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "object": self.object,
            "form": form
        }
        return TemplateResponse(self.request, 'htmx/create.html', context)

    def form_invalid(self, form):
        super().form_invalid(form)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(self.request, 'htmx/form.html', context)


class HTMXDrugDeleteView(generic.DeleteView):
    model = models.Drug
    success_url = reverse_lazy("PharmaPrices_Drug_htmx_list")
    
    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()