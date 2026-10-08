from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Account, Expense




router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)




@router.get("/{user_id}")
def dashboard(
    user_id: int,
    db: Session = Depends(get_db)
):

    # Get accounts
    accounts = db.query(Account).filter(
        Account.user_id == user_id
    ).all()


    # Get expenses
    expenses = db.query(Expense).filter(
        Expense.user_id == user_id
    ).all()


    # Total balance
    total_balance = 0

    for account in accounts:

        total_balance += account.balance


    # Total expenses
    total_expenses = 0

    for expense in expenses:

        total_expenses += expense.amount


    # Remaining balance
    remaining_balance = total_balance


    return {
        "total_balance": total_balance,
        "total_expenses": total_expenses,
        "remaining_balance": remaining_balance
    }