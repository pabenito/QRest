import pytest
from fastapi import status
from fastapi.testclient import TestClient
from fastapi.exceptions import HTTPException

from app.api.backend.order import router
from app.lib.utils import json_lower_encoder

client = TestClient(router)


def test_get_current_command__when_current_command_exists__then_return_current_command():
    pass


def test_get_current_command__when_order_does_not_exists__then_http_status_not_found():
    pass


def test_get_current_command__when_current_command_does_not_exists__then_return_empty_list():
    pass


def test_confirm_current_command__when_command_exists__then_return_command():
    pass


def test_confirm_current_command__when_order_does_not_exists__then_http_status_404_not_found():
    pass


def test_confirm_current_command__when_current_command_does_not_exists__then_http_status_400_bad_request():
    pass


def test_add_element__when_element_is_correct__then_added_to_the_order():
    pass


def test_add_element__when_order_does_not_exists__then_http_status_not_found():
    pass


def test_add_element__when_element_is_not_correct__then_http_status_422_unprocessable_entity():
    pass


def test_remove_element__when_element_is_correct__then_is_removed_from_the_order():
    pass


def test_remove_element__when_order_does_not_exists__then_http_status_not_found():
    pass


def test_remove_element__when_element_is_not_correct__then_http_status_422_unprocessable_entity():
    pass


def test_remove_element__when_element_does_not_exists__then_http_status_400_bad_request():
    pass
