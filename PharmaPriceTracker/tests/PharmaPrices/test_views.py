import pytest
import test_helpers

from django.urls import reverse
from datetime import datetime


pytestmark = [pytest.mark.django_db]


def tests_Company_list_view(client):
    instance1 = test_helpers.create_PharmaPrices_Company()
    instance2 = test_helpers.create_PharmaPrices_Company()
    url = reverse("PharmaPrices_Company_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Company_create_view(client):
    url = reverse("PharmaPrices_Company_create")
    data = {
        "name": "text",
        "website": 'http://127.0.0.1',
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Company_detail_view(client):
    instance = test_helpers.create_PharmaPrices_Company()
    url = reverse("PharmaPrices_Company_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Company_update_view(client):
    instance = test_helpers.create_PharmaPrices_Company()
    url = reverse("PharmaPrices_Company_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "website": 'http://127.0.0.1',
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_DataPoint_list_view(client):
    instance1 = test_helpers.create_PharmaPrices_DataPoint()
    instance2 = test_helpers.create_PharmaPrices_DataPoint()
    url = reverse("PharmaPrices_DataPoint_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_DataPoint_create_view(client):
    drug = test_helpers.create_PharmaPrices_Drug()
    url = reverse("PharmaPrices_DataPoint_create")
    data = {
        "price": "text",
        "date": datetime.now(),
        "drug": drug.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_DataPoint_detail_view(client):
    instance = test_helpers.create_PharmaPrices_DataPoint()
    url = reverse("PharmaPrices_DataPoint_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_DataPoint_update_view(client):
    drug = test_helpers.create_PharmaPrices_Drug()
    instance = test_helpers.create_PharmaPrices_DataPoint()
    url = reverse("PharmaPrices_DataPoint_update", args=[instance.pk, ])
    data = {
        "price": "text",
        "date": datetime.now(),
        "drug": drug.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Drug_list_view(client):
    instance1 = test_helpers.create_PharmaPrices_Drug()
    instance2 = test_helpers.create_PharmaPrices_Drug()
    url = reverse("PharmaPrices_Drug_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Drug_create_view(client):
    company = test_helpers.create_PharmaPrices_Company()
    url = reverse("PharmaPrices_Drug_create")
    data = {
        "name": "text",
        "description": "text",
        "website": 'http://127.0.0.1',
        "company": company.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Drug_detail_view(client):
    instance = test_helpers.create_PharmaPrices_Drug()
    url = reverse("PharmaPrices_Drug_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Drug_update_view(client):
    company = test_helpers.create_PharmaPrices_Company()
    instance = test_helpers.create_PharmaPrices_Drug()
    url = reverse("PharmaPrices_Drug_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "description": "text",
        "website": 'http://127.0.0.1',
        "company": company.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
