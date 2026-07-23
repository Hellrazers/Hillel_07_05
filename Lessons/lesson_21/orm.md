# Шпоргалка з SQLAlchemy 2.0: Базові та розширені операції

Цей посібник містить практичні приклади використання **SQLAlchemy 2.0** для роботи з реляційними базами даних у Python: від створення моделей до виконання складних запитів.

---

## 1. Налаштування підключення та оголошення моделей

У SQLAlchemy 2.0 створення моделей відбувається шляхом успадкування від класу `DeclarativeBase`.

```python
from typing import List, Optional
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

# 1. Ініціалізація Engine та сесії
DATABASE_URL = "sqlite:///:memory:"  # або "postgresql://user:pass@localhost/dbname"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)


# 2. Базовий клас для моделей
class Base(DeclarativeBase):
    pass


# 3. Моделі з відношенням One-to-Many
class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    # Зв'язок зі співробітниками
    employees: Mapped[List["Employee"]] = relationship(
        "Employee", back_populates="department"
    )


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(Integer)
    salary: Mapped[int] = mapped_column(Integer)
    department_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("departments.id")
    )

    # Зв'язок з департаментом
    department: Mapped[Optional[Department]] = relationship(
        "Department", back_populates="employees"
    )


# Створення всіх таблиць у БД
Base.metadata.create_all(engine)
```

---

## 2. CRUD Операції (Create, Read, Update, Delete)

### 2.1 Створення даних (Insert)

#### Додавання одного об'єкта:
```python
with SessionLocal() as session:
    dev_dept = Department(name="IT")
    session.add(dev_dept)
    session.commit()
```

#### Масове додавання (Bulk Insert):
Для вставки кількох записів за один раз передається **список словників (`list[dict]`)**:
```python
from sqlalchemy import insert

with SessionLocal() as session:
    stmt = insert(Employee).values([
        {"name": "Alice", "age": 25, "salary": 3000, "department_id": 1},
        {"name": "Bob", "age": 28, "salary": 3500, "department_id": 1},
        {"name": "Charlie", "age": 17, "salary": 1200, "department_id": 1},
    ])
    session.execute(stmt)
    session.commit()
```

---

### 2.2 Читання даних (Select)

#### Отримання всіх записів або одного запису:
```python
from sqlalchemy import select

with SessionLocal() as session:
    # Отримати всіх співробітників
    stmt = select(Employee)
    employees = session.scalars(stmt).all()

    # Отримати одного співробітника за умовою
    stmt_single = select(Employee).where(Employee.name == "Alice")
    alice = session.scalars(stmt_single).first()
```

> **Примітка:** `session.scalars()` розпаковує об'єкти з першої колонки запиту, повертаючи чисті об'єкти ORM замість кортежів.

---

### 2.3 Оновлення даних (Update)

#### Оновлення конкретного об'єкта (через ORM):
```python
with SessionLocal() as session:
    emp = session.scalars(select(Employee).where(Employee.id == 1)).first()
    if emp:
        emp.salary = 3200
        session.commit()
```

#### Масове оновлення (Bulk Update):
```python
from sqlalchemy import update

with SessionLocal() as session:
    # Підняти вік до 18 для всіх неповнолітніх з id > 5
    stmt = (
        update(Employee)
        .where(Employee.age < 18, Employee.id > 5)  # Декілька умов через кому = AND
        .values(age=18)
    )
    session.execute(stmt)
    session.commit()
```

---

### 2.4 Видалення даних (Delete)

```python
from sqlalchemy import delete

with SessionLocal() as session:
    stmt = delete(Employee).where(Employee.age < 18)
    session.execute(stmt)
    session.commit()
```

---

## 3. Фільтрація, Сортування та Пагінація

### 3.1 Поєднання умов (`AND`, `OR`)

* **Логічне `AND`**: Передаються умови через кому у `.where(...)` або через `&` з дужками `()`.
* **Логічне `OR`**: Використовується функція `or_()` або оператор `|` з дужками `()`.

```python
from sqlalchemy import and_, or_, select

# Варіант 1: Через кому (автоматично AND)
stmt1 = select(Employee).where(Employee.age >= 18, Employee.salary > 2000)

# Варіант 2: З операторами & та | (ОБОВ'ЯЗКОВІ дужки!)
stmt2 = select(Employee).where((Employee.age >= 18) & (Employee.salary > 2000))

# Варіант 3: Логічне OR
stmt3 = select(Employee).where(or_(Employee.age < 20, Employee.salary > 5000))
```

---

### 3.2 Сортування (`order_by`)

```python
from sqlalchemy import select

# За зростанням (ASC) та спаданням (DESC)
stmt = (
    select(Employee)
    .where(Employee.salary > 1000)
    .order_by(Employee.salary.desc(), Employee.name.asc())
)
```

---

### 3.3 Пагінація (`limit` & `offset`)

```python
page = 2
page_size = 10
calculate_offset = (page - 1) * page_size

stmt = (
    select(Employee)
    .order_by(Employee.id)  # Сортування обов'язкове для стабільної пагінації
    .limit(page_size)
    .offset(calculate_offset)
)
```

---

## 4. Об'єднання таблиць (JOINs)

При використанні `.join(Model)` таблиця з `select(...)` опиняється **зліва (FROM)**, а таблиця з `.join(...)` — **справа (JOIN)**.

### 4.1 INNER JOIN

```python
from sqlalchemy import select

# Поверне об'єкти Employee, які мають зв'язаний Department
stmt = (
    select(Employee)
    .join(Department, Employee.department_id == Department.id)
    .where(Department.name == "IT")
)

employees = session.scalars(stmt).all()
```

### 4.2 LEFT OUTER JOIN

```python
# Поверне всіх працівників, навіть якщо department_id == None
stmt = select(Employee, Department).outerjoin(
    Department, Employee.department_id == Department.id
)

results = session.execute(stmt).all()
# results: [ (<Employee>, <Department>), (<Employee>, None), ... ]
```

---

## 5. Скалярні підзапити (`scalar_subquery`)

Скалярний підзапит повертає **одне значення** (один рядок і одна колонка), яке можна використати для порівнянь чи обчислень всередині іншого запиту.

```python
from sqlalchemy import func, select

# 1. Підзапит: розрахунок середньої зарплати
avg_salary_subquery = select(func.avg(Employee.salary)).scalar_subquery()

# 2. Основний запит: працівники із зарплатою вище середньої
stmt = select(Employee).where(Employee.salary > avg_salary_subquery)

rich_employees = session.scalars(stmt).all()
```

---

## 6. Pytest Фікстури для тестування (QA Automation)

Приклад організації фікстур у `conftest.py` для ізоляції тестових даних та автоочищення бази:

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="session")
def engine():
    _engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(_engine)
    yield _engine
    Base.metadata.drop_all(_engine)
    _engine.dispose()


@pytest.fixture(scope="function")
def db_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.rollback()  # Відкот усіх змін після тесту
    session.close()
```

### Приклад тесту (`test_employees.py`):
```python
def test_create_employee(db_session):
    new_emp = Employee(name="John", age=30, salary=4000)
    db_session.add(new_emp)
    db_session.commit()

    saved_emp = db_session.scalars(
        select(Employee).where(Employee.name == "John")
    ).first()

    assert saved_emp is not None
    assert saved_emp.salary == 4000
```