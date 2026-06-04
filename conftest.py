import pytest
from api.courier_api import CourierApi

@pytest.fixture
def cleanup_courier():
    courier_id = []

    yield courier_id 
    
    courier_api = CourierApi()

    for id in courier_id:
        courier_api.delete_courier_and_return_response(
            courier_id
        )

@pytest.fixture
def created_courier():

    courier_api = CourierApi()

    response, payload = (
        courier_api.register_new_courier_and_return_response()
    )

    return payload

