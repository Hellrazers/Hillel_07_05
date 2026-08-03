from typing import List, Dict, Any, Self

from pydantic import BaseModel, field_validator, Field, model_validator, ConfigDict

json_obj = {
    "status": "success",
    'as': 123,
    "data": [
        {
            "id": 1,
            "name": "Oleksii",
            "email": "oleksii@example.com",
            "is_active": True,
            "age": 19,
            "user_params":  {
                "id": 1,
                "value": 'asdasd'
            },

        },
        {
            "id": 1,
            "name": None,
            "email": "ivan@example.com",
            "is_active": True,
            "age": 19

        },
        {
            "id": 3,
            "name": "Marta",
            "email": "marta@example.com",
            "is_active": False,
            "age": 19
        },
        {
            "id": 4,
            "name": 123,
            "email": "marta@example.com",
            "is_active": False,
            "age": 19,
            "user_params": None
        },
    ]
}
# status  = null -> None
class UserParams(BaseModel):

    id: int
    value: str


class User(BaseModel):
    id: int
    email: str

    is_active: bool
    age: int = Field(ge=18)
    user_params: UserParams | None = None

    name: str | None | int

    @field_validator('email')
    @classmethod
    def validate(cls, value: Any):
        if value.count('@') == 0:
            raise ValueError('Email should contain @')
        if value.count('@') > 1:
            raise ValueError('Email should have 1 @')

        return value


class Data(BaseModel):
    data: List[User]
    model_config = ConfigDict(extra='ignore')

    @model_validator(mode='after')
    def uniq_id(self) -> Self:
        set_id = set()
        list_of_errors = list()
        for user in self.data:
            if user.id not in set_id:
                set_id.add(user.id)
            else:
                list_of_errors.append(user.id)
        if list_of_errors:
            raise ValueError(f"We have not uniq ids for this values: {list_of_errors}")
        return self




# for user in json_obj.get('users'):
#     assert isinstance(user.get('id'), int)
#     assert isinstance(user.get('name'), str)
#     assert isinstance(user.get('email'), str)


# for user in json_obj:
#     print(User.model_validate(json_2))
model_users = Data.model_validate(json_obj)
# print(model_users.data[-1].id)
# print(model_users.data[0].user_params.value == json_obj.get('data')[0].get('user_params').get('value'))
print(model_users.data)


#
# json_obj = { "carBrandId" : 1,
#              "carBrandId.asdasd.carBrandId": 2 }
#
# class Car(BaseModel):
#     car_brand_id: int = Field(alias='carBrandId')
#     carBrandId_asdasd_carBrandId: Field(alias='carBrandId.asdasd.carBrandId')