import pytest
import allure
from allure_commons.types import LinkType, LabelType

from models.car_model.car_payload import CarPost
from tests.api_tests.car_tests import DefValuesCar


@allure.epic('ED-14: Машини')
@allure.story("ED-34: Створити ендпоінт для ГЕТ ")
@allure.feature('ED-55: Можливість гет усіх машин')
@allure.link(url='jira-board/ed-14', name='ED-14: Машини', link_type=LinkType.LINK)
@allure.link(url='jira-board/ed-34', name='ED-34: Створити ендпоінт для ГЕТ ', link_type=LinkType.ISSUE)
@allure.link(url='jira-board/ed-55', name='ED-55: Можливість гет усіх машин', link_type=LinkType.TEST_CASE)
@pytest.mark.api_test
class DefGetCar:
    pass


class TestCarGet(DefGetCar):
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('''Цей тест робить запит GET /cars 
    І далі ми валідуємо щось''')
    @allure.title('Get всіх машин за допомогою парсинга респонса PY')
    def test_with_py(self, api):
        resp = api.car.get_car_py()
        assert resp.status_code == 200
        assert resp.data[0].brand == "Audi"
        payload_to_create_car = CarPost(
            carBrandId=1,
            carModelId=1,
            mileage=133
        )
        resp_create = api.car.post_car_py(payload_to_create_car)
        # response_car.json().get('data')[0].get('brand')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Get всіх машин')
    def test_car_test(self, api):
        '''Цей тест робить запит GET /cars
        І далі ми валідуємо щось'''
        print(api.brand.base_url)
        response_car = api.car.get_car()
        post_car = api.car.post_car(our_payload={"carBrandId": 1, "carModelId": 1, "mileage": 122})
        car_id = post_car.json().get('data').get('id')
        car_id_to_delete = api.car.delete_car(car_id)
        car_reps_id = api.car.get_car_by_id(car_id, 404)
        # requests.post('https://qauto.forstudy.space/api/cars', json={'carBrandId': 1, 'carModelId': 1, 'mileage': 122}, cookies={'sid': "s%3AR_KNsnZ9UzornjRAFuUWLd-dfcW8BSjS.e6XGK5BGs1sB8C%2FOzXBMla78%2BchTA5LOF1v7KkV23Mw"})


@allure.epic('asdasdasd')
@allure.story("ED-33:  Create car ")
@allure.feature('ED-45:  машинa sdasd')
class TestCarCreate(DefValuesCar):

    @allure.description('''Pre-condition:
    Створюємо машину  
    Test Body:
    Ми гетамємо створену машини з Pre-cond
    Post cond:
    Видаляємо машини з Pre-cond
       ''')
    @allure.title("Гет існуючою машини")
    # @allure.label(LabelType.LANGUAGE, "python")
    def test_car_by_id(self, crate_and_delete_car):
        api, response_create_car = crate_and_delete_car
        allure.dynamic.title(f'Гет кар бай айді {response_create_car.json().get('data').get('id')}')

        # with allure.step(f'Робимо гет по /car/{response_create_car.json().get('data').get('id')}'):
        car_id = response_create_car.json().get('data').get('id')
        car_reps_id = api.car.get_car_by_id(car_id)
        with allure.step('Валідація чи айді збігаются'):
            assert car_reps_id.json().get('data').get('id') == car_id


@allure.story("ED-66:  Delete  car ")
@allure.feature('ED-345:  машинa sdasd')
class TestCarDelete(DefValuesCar):
    @allure.title('Видалення машини')
    def test_delete_car(self, delete_car):
        api, list_obj_to_delete = delete_car
        post_car = api.car.post_car(our_payload={"carBrandId": 1, "carModelId": 1, "mileage": 122})
        post_car_1 = api.car.post_car(our_payload={"carBrandId": 1, "carModelId": 1, "mileage": 122})
        list_obj_to_delete += [post_car, post_car_1]

    @allure.title('Видалення всіх машин')
    def test_delete_all_car(self, api):
        response_car = api.car.get_car()
        for car in response_car.json().get('data'):
            api.car.delete_car(item_id=int(car.get('id')))

    @allure.title('Видалення всіх машин з Py')

    def test_delete_all_car_pl(self, api_pl):
        response_car = api_pl.get('/api/cars')
        assert response_car.status == 200
        for car in response_car.json().get('data'):
            api_pl.delete(f'/api/cars/{car.get('id')}')
            response_get_by_id = api_pl.get(f'/api/cars/{car.get('id')}')
            assert response_get_by_id.status == 404
        response_car_after_delete = api_pl.get('/api/cars')
        assert len(response_car_after_delete.json().get('data')) == 0
