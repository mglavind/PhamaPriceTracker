import random
import string

from datetime import datetime

from PharmaPrices import models as PharmaPrices_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_PharmaPrices_Company(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["website"] = ""
    defaults["description"] = ""
    defaults.update(**kwargs)
    return PharmaPrices_models.Company.objects.create(**defaults)
def create_PharmaPrices_DataPoint(**kwargs):
    defaults = {}
    defaults["price"] = ""
    defaults["date"] = datetime.now()
    if "drug" not in kwargs:
        defaults["drug"] = create_PharmaPrices_Drug()
    defaults.update(**kwargs)
    return PharmaPrices_models.DataPoint.objects.create(**defaults)
def create_PharmaPrices_Drug(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["description"] = ""
    defaults["website"] = ""
    if "company" not in kwargs:
        defaults["company"] = create_PharmaPrices_Company()
    defaults.update(**kwargs)
    return PharmaPrices_models.Drug.objects.create(**defaults)
