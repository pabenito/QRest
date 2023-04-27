from pprint import pprint

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from fastapi.exceptions import RequestValidationError, HTTPException
from bson import ObjectId
from app.utils import json_lower_encoder
from .allergens import router

client = TestClient(router)


def test_get___when_get___then_get_all_allergens():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == allergens


allergens = [
    {
        "name": "altramuces",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504399/allergens/altramuces_b4jvje.png",
    },
    {
        "name": "apio",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/apio_pl5hsf.png",
    },
    {
        "name": "cacahuetes",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/cacahuetes_wgnv6b.png",
    },
    {
        "name": "crustaceos",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/crustaceos_jbhopr.png",
    },
    {
        "name": "frutos de cascara",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/frutos_de_cascara_vxancr.png",
    },
    {
        "name": "gluten",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/gluten_c6tk3b.png",
    },
    {
        "name": "huevo",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/huevo_v41h5a.png",
    },
    {
        "name": "lacteos",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504398/allergens/lacteos_wxgwnp.png",
    },
    {
        "name": "moluscos",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/moluscos_e9wa3o.png",
    },
    {
        "name": "mostaza",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/mostaza_ib5sik.png",
    },
    {
        "name": "pescado",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/pescado_nwumbp.png",
    },
    {
        "name": "sesamo",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/sesamo_xae3sh.png",
    },
    {
        "name": "soja",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/soja_ictpzn.png",
    },
    {
        "name": "sulfitos",
        "icon": "https://res.cloudinary.com/dteqcnpp3/image/upload/v1682504397/allergens/sulfitos_yhraaz.png",
    },
]