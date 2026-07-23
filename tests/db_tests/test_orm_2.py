import time
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.sql.expression import update, select

from contract.db.db import session
from contract.db.orm_department_table import OrmDepartment
from contract.db.orm_employee_table import OrmEmployee
from contract.db.orm_user_table import OrmUser


# Створення таблиць у базі даних

def test_sq():
    time_ = time.time()
    result_1 = session.scalars(select(OrmUser)).all()

    list_age = [k.age for k in result_1]

    avr_age = sum(list_age) / len(list_age)
    print(f'OUR AVARGE AGE = {avr_age}')
    result_1 = session.scalars(select(OrmUser).where(OrmUser.age > avr_age )).all()

    for k in result_1:
        print(k)

    # avg_age_subquery = select(func.avg(OrmUser.age)).scalar_subquery()
    #
    # # 2. Основний запит: працівники із зарплатою вище середньої
    # stmt = select(OrmUser).where(OrmUser.age > avg_age_subquery)
    #
    # rich_employees = session.scalars(stmt).all()
    # for employee in rich_employees:
    #     print(employee)

    datetime_now = time.time() - time_
    print(datetime_now)

#0.04579782485961914


#0.030727148056030273



def test_forg_key():


    session.execute(update(OrmDepartment).where(OrmDepartment.id == 2 ).values(name='Teacher'))
    session.commit()

    query_1 = select(OrmEmployee).join(OrmDepartment)
    # print(query_1)
    # print(session.scalars(query_1).all())

    query_2 = (select(OrmUser, OrmEmployee).join(OrmEmployee, OrmUser.id == OrmEmployee.id)
               .where(OrmEmployee.department_id == 3))
    result_join = session.scalars(query_2).all()
    result_join_2 = session.execute(query_2).all()

    for user, employee in result_join_2:

        assert user.id == employee.id
    # Base.metadata.create_all(engine)
    #
    # # Додавання департаментів та співробітників до бази даних
    # it_department = OrmDepartment(name='IT')
    # hr_department = OrmDepartment(name='HR')
    #
    # john = OrmEmployee(name='John', department=it_department)
    # alice = OrmEmployee(name='Alice', department=hr_department)
    # bob = OrmEmployee(name='Bob', department=it_department)
    #
    # session.add_all([it_department, hr_department, john, alice, bob])
    # session.commit()

    # # Вибірка співробітників та їх департаментів
    # employees = session.query(OrmEmployee).all()
    # for employee in employees:
    #     print(f"Ім'я: {employee.name}, Департамент: {employee.department.name}")

    # Закриття сесії
