from core.api_session import ApiSession


class CarRequest(ApiSession):
    def __init__(self):
        self.api = ApiSession()
        self.path = '/api/cars'

    def get_car(self,params: dict = None, status_code : int = 200):
        resp = self.api.get(params=params, path=self.path)
        assert resp.status_code == status_code, f'status code is not {status_code}'

        return resp

    def post_car(self, our_payload: dict, status_code : int = 201):
       resp = self.api.post(data=our_payload, path=self.path)
       assert resp.status_code == status_code, f'status code is not {status_code}'
       return resp

    def delete_car(self, item_id: dict, status_code : int = 200):
        resp = self.api.delete(path=f'{self.path}/{item_id}')
        assert resp.status_code == status_code, f'status code is not {status_code}'
        return resp

    def get_car_by_id(self, item_id: dict, status_code : int = 200):
        resp = self.api.get(path=f'{self.path}/{item_id}')
        assert resp.status_code == status_code, f'status code is not {status_code}'
        return resp