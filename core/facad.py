from contract.api.brand import BrandRequest
from contract.api.car import CarRequest
from core.api_session import ApiSession


class ApiClient:
    def __init__(self, token = None):
        self.api = ApiSession(token=token)
        self.car = CarRequest()
        self.brand = BrandRequest()
        self.user = None