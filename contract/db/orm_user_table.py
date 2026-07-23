

from sqlalchemy import Column, Integer, String
from contract.db.db import Base



# Визначення моделі даних (таблиці) за допомогою класу
class OrmUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"OrmUser::id: {self.id}, name: {self.name}, age: {self.age}"


