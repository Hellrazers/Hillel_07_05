import faker
import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import select, insert, update
from sqlalchemy.sql.operators import and_

from contract.db.db import Base, engine, session
from contract.db.orm_user_table import OrmUser
from faker import Faker
import random


f = Faker()



@pytest.mark.db_test
def test_update():
    user_id = random.choice(range(15,180))
    exp_name = f.first_name()
    exp_age =  random.choice(range(5,99))
    user_query = select(OrmUser).where((OrmUser.id == user_id))


    exp_user_result = session.scalars(user_query).first()

    name_user = exp_user_result.name
    age = exp_user_result.age

    user_update_query = (update(OrmUser).where(OrmUser.id == user_id)
                         .values(name=exp_name, age=exp_age))
    session.execute(user_update_query)
    session.commit()


    ar_user_result = session.scalars(select(OrmUser).where((OrmUser.id == user_id))).first()
    assert ar_user_result.name != name_user
    assert ar_user_result.age != age
    assert ar_user_result.name == exp_name
    assert ar_user_result.age == exp_age
    assert ar_user_result.id == user_id



@pytest.mark.db_test
# Додавання нового користувача
def test_orm():
    # Base.metadata.create_all(engine)

    #Додавання Юзера
    # new_user = [OrmUser(name=f.name(), age=random.choice(range(18, 80))) for k in range(10)]
    # session.add_all(new_user)
    #
    # new_user_2 = [{'name': f.name(), 'age': random.choice(range(18, 80))} for k in range(10)]
    # print(new_user_2)
    # insert_user = insert(OrmUser).values(new_user_2)
    # session.execute(insert_user)
    # session.commit()

    # session.rollback()
    # Відповідає INSERT INTO users (name, age) VALUES ('John', 30);


    # Отримання Днних через select users where age > 30 and startswith(name)==Br
    user_2  = select(OrmUser).where((OrmUser.age > 30) & (OrmUser.name.startswith("Br")))
    user = select(OrmUser).where(and_
                                 (OrmUser.age > 30,
                                  OrmUser.name.startswith("Br")))

    result = session.scalars(user).all()
    result_2 = session.scalars(user_2).all()
    for user in result:
        print(f'ID - {user.id}, Name - {user.name}, Age - {user.age}')

    assert result_2 == result
    for index, user in enumerate(result):
        print(user)
        assert user.id == result[index].id
        assert user.name == result[index].name
        assert user.age == result[index].age
    # result_2 = session.execute(user).all()
    # print(result_2)
    # print(result)
    # user = session.query(OrmUser).filter_by(name='John').first()
    # user.age = 31
    # session.commit()
    # Відповідає UPDATE users SET age=31 WHERE name='John';

    # Видалення користувача
    # session.delete(user)
    # session.commit()
    # Відповідає DELETE FROM users WHERE name='John';


    #
    # # Вибірка всіх користувачів
    # all_users = session.query(User).all()
    # # SQL аналог: SELECT * FROM users;
    #
    # # Фільтрація за умовою
    # john = session.query(User).filter_by(name='John').first()
    # # SQL аналог: SELECT * FROM users WHERE name = 'John' LIMIT 1;
    #
    # # Сортування
    # sorted_users = session.query(User).order_by(User.age.desc()).all()
    # # SQL аналог: SELECT * FROM users ORDER BY age DESC;