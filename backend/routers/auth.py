from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from database import get_db
from models import User
from schemas import UserCreate, UserLogin


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)




@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    hashed_password = pwd_context.hash(
        user.password
    )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Account created",
        "user_id": new_user.id
    }




@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user is None:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    if not pwd_context.verify(
        user.password,
        existing_user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Wrong password"
        )

    return {
        "message": "Login successful",
        "user_id": existing_user.id,
        "username": existing_user.username
    }