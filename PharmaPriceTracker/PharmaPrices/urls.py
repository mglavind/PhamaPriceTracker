from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("Company", api.CompanyViewSet)
router.register("DataPoint", api.DataPointViewSet)
router.register("Drug", api.DrugViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("PharmaPrices/Company/", views.CompanyListView.as_view(), name="PharmaPrices_Company_list"),
    path("PharmaPrices/Company/create/", views.CompanyCreateView.as_view(), name="PharmaPrices_Company_create"),
    path("PharmaPrices/Company/detail/<int:pk>/", views.CompanyDetailView.as_view(), name="PharmaPrices_Company_detail"),
    path("PharmaPrices/Company/update/<int:pk>/", views.CompanyUpdateView.as_view(), name="PharmaPrices_Company_update"),
    path("PharmaPrices/Company/delete/<int:pk>/", views.CompanyDeleteView.as_view(), name="PharmaPrices_Company_delete"),
    path("PharmaPrices/DataPoint/", views.DataPointListView.as_view(), name="PharmaPrices_DataPoint_list"),
    path("PharmaPrices/DataPoint/create/", views.DataPointCreateView.as_view(), name="PharmaPrices_DataPoint_create"),
    path("PharmaPrices/DataPoint/detail/<int:pk>/", views.DataPointDetailView.as_view(), name="PharmaPrices_DataPoint_detail"),
    path("PharmaPrices/DataPoint/update/<int:pk>/", views.DataPointUpdateView.as_view(), name="PharmaPrices_DataPoint_update"),
    path("PharmaPrices/DataPoint/delete/<int:pk>/", views.DataPointDeleteView.as_view(), name="PharmaPrices_DataPoint_delete"),
    path("PharmaPrices/Drug/", views.DrugListView.as_view(), name="PharmaPrices_Drug_list"),
    path("PharmaPrices/Drug/create/", views.DrugCreateView.as_view(), name="PharmaPrices_Drug_create"),
    path("PharmaPrices/Drug/detail/<int:pk>/", views.DrugDetailView.as_view(), name="PharmaPrices_Drug_detail"),
    path("PharmaPrices/Drug/update/<int:pk>/", views.DrugUpdateView.as_view(), name="PharmaPrices_Drug_update"),
    path("PharmaPrices/Drug/delete/<int:pk>/", views.DrugDeleteView.as_view(), name="PharmaPrices_Drug_delete"),

    path("PharmaPrices/htmx/Company/", htmx.HTMXCompanyListView.as_view(), name="PharmaPrices_Company_htmx_list"),
    path("PharmaPrices/htmx/Company/create/", htmx.HTMXCompanyCreateView.as_view(), name="PharmaPrices_Company_htmx_create"),
    path("PharmaPrices/htmx/Company/delete/<int:pk>/", htmx.HTMXCompanyDeleteView.as_view(), name="PharmaPrices_Company_htmx_delete"),
    path("PharmaPrices/htmx/DataPoint/", htmx.HTMXDataPointListView.as_view(), name="PharmaPrices_DataPoint_htmx_list"),
    path("PharmaPrices/htmx/DataPoint/create/", htmx.HTMXDataPointCreateView.as_view(), name="PharmaPrices_DataPoint_htmx_create"),
    path("PharmaPrices/htmx/DataPoint/delete/<int:pk>/", htmx.HTMXDataPointDeleteView.as_view(), name="PharmaPrices_DataPoint_htmx_delete"),
    path("PharmaPrices/htmx/Drug/", htmx.HTMXDrugListView.as_view(), name="PharmaPrices_Drug_htmx_list"),
    path("PharmaPrices/htmx/Drug/create/", htmx.HTMXDrugCreateView.as_view(), name="PharmaPrices_Drug_htmx_create"),
    path("PharmaPrices/htmx/Drug/delete/<int:pk>/", htmx.HTMXDrugDeleteView.as_view(), name="PharmaPrices_Drug_htmx_delete"),
    path('search-item/', views.search_item, name='search-item'),
)
