
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from contract.db.db import Base


# Визначення моделей даних (таблиць) за допомогою класів
class OrmDepartment(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("OrmEmployee", back_populates="department")


    def __repr__(self):
        return f"{self.name}"