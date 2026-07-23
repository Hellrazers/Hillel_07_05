
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from contract.db.db import Base

class OrmEmployee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("OrmDepartment", back_populates="employees")


    def __repr__(self):
        return f"OrmEmployee::id={self.id}:name={self.name}:department={self.department}"