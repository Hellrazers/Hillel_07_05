import pytest

from core.facad import ApiClient


@pytest.fixture(scope="session")
def api() -> ApiClient:
    return ApiClient()


@pytest.fixture
def create_car(api):
    payload = {"carBrandId": 1,"carModelId": 1,"mileage": 122}
    post_car_response = api.car.post_car(our_payload=payload)
    return api, post_car_response


@pytest.fixture
def delete_car(api):
    list_obj_to_delete = []
    yield api, list_obj_to_delete
    if list_obj_to_delete:
        for resp in list_obj_to_delete:
            car_id = resp.json().get('data').get('id')
            car_id_to_delete = api.car.delete_car(car_id)
            car_reps_id = api.car.get_car_by_id(car_id, 404)

@pytest.fixture
def crate_and_delete_car(create_car):
    api , post_car_response = create_car
    yield api, post_car_response
    car_id = post_car_response.json().get('data').get('id')
    car_id_to_delete = api.car.delete_car(car_id)
    car_reps_id = api.car.get_car_by_id(car_id, 404)

