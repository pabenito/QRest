# Import libraries
from pprint import pprint

from fastapi import APIRouter, status, HTTPException
from datetime import datetime
from app.database import db
from app.entities.models import Order, OrderId
from app.utils import json_lower_encoder, remove_non_letters_and_replace_spaces

# Create router
router = APIRouter()

# Collections
orders = db["orders"]

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OrderId, response_model_exclude_unset=True)
def create_order(order: Order):
    order.created = datetime.now()
    order_dict = json_lower_encoder(order)
    new_order = orders.insert_one(order_dict)
    created_order = orders.find_one({"_id": new_order.inserted_id})

    return created_order