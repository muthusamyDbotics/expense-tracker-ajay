from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str



class UserLogin(BaseModel):
    username: str
    password: str




class AccountCreate(BaseModel):
    account_name: str
    account_type: str
    balance: float
    user_id: int




class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    description: str | None = None
    date: str
    account_id: int
    user_id: int