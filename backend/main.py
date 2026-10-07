from fastapi import FastAPI , Depends
from schemas import ExpenseCreate as expense_create
from sqlalchemy.orm import Session
from database import SessionLocal 
from models import Expense

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/expenses", response_model=expense_create)
def create_expense(expense: expense_create , db: Session = Depends(get_db)):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh()
    return db_expense