from pydantic import BaseModel


class expenseBase(BaseModel):
    title: str
    amount: float
    date: date
    category: str
    
class expenseCreate(expenseBase):
    pass

class expenseResponse(expenseBase):
    id: int 
    class Config:
        orm_mode = True