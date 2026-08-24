from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних

# def db_url(db_type, user, password, host='localhost', port=5432):
DATABASE_URL = "postgresql://teacher:super_password@172.23.48.1:5432/education_platform"
engine = create_engine(DATABASE_URL)
# Базовий клас для визначення моделей даних
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()