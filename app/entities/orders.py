# Import libraries
from pprint import pprint

import pymongo
from bson import ObjectId
from fastapi import APIRouter, status, HTTPException
from datetime import datetime
from app.database import db
from app.entities.models import Order, OrderId
from app.utils import json_lower_encoder, remove_non_letters_and_replace_spaces

# Create router
router = APIRouter()

# Collections
orders = db["orders"]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OrderId, response_model_exclude_unset=True,
             response_model_by_alias=False)
def create_order(order: Order):
    order.created = datetime.now()
    order_dict = json_lower_encoder(order)
    new_order = orders.insert_one(order_dict)
    created_order = orders.find_one({"_id": new_order.inserted_id})

    return created_order


@router.get("/", response_model=list[OrderId], response_model_exclude_unset=True, response_model_by_alias=False)
def get_orders():
    return list(orders.find().sort("created", pymongo.DESCENDING))


@router.get("/{id}", response_model=OrderId, response_model_exclude_unset=True, response_model_by_alias=False)
def get_order(id: str):
    return _get_order(id)

@router.delete("/{id}", response_model=Order, response_model_exclude_unset=True, response_model_by_alias=False)
def delete_order(id: str):
    order = _get_order(id)
    orders.delete_one({"_id": id})
    return order


def _get_order(id: str):
    order = orders.find_one({"_id": ObjectId(id)})
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El pedido '{id}', no existe.")
    return order
