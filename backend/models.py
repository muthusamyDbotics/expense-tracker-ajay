from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)



class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String, nullable=False)
    account_type = Column(String, nullable=False)
    balance = Column(Float, nullable=False)
    user_id = Column(Integer, nullable=False)


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(String, nullable=False)
    account_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)