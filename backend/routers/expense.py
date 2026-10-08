from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Expense, Account
from schemas import ExpenseCreate


router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)




@router.post("/")
def add_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db)
):

   
    account = db.query(Account).filter(
        Account.id == expense.account_id
    ).first()

    
    account.balance = (
        account.balance - expense.amount
    )

    
    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        date=expense.date,
        account_id=expense.account_id,
        user_id=expense.user_id
    )

    db.add(new_expense)

    db.commit()

    db.refresh(new_expense)

    return {
        "message": "Expense added",
        "expense_id": new_expense.id
    }



@router.get("/{user_id}")
def get_expenses(
    user_id: int,
    db: Session = Depends(get_db)
):

    expenses = db.query(Expense).filter(
        Expense.user_id == user_id
    ).all()

    return expenses