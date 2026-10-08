from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Account
from schemas import AccountCreate


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)



@router.post("/")
def add_account(
    account: AccountCreate,
    db: Session = Depends(get_db)
):

    new_account = Account(
        account_name=account.account_name,
        account_type=account.account_type,
        balance=account.balance,
        user_id=account.user_id
    )

    db.add(new_account)

    db.commit()

    db.refresh(new_account)

    return {
        "message": "Account added",
        "account_id": new_account.id
    }



@router.get("/{user_id}")
def get_accounts(
    user_id: int,
    db: Session = Depends(get_db)
):

    accounts = db.query(Account).filter(
        Account.user_id == user_id
    ).all()

    return accounts