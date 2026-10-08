from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pwdlib import PasswordHash

from database import get_db
from models import User
from schemas import UserCreate, UserLogin


# Create authentication router
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Password hashing
password_hash = PasswordHash.recommended()



@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    # Check if username already exists
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Check if email already exists
    existing_email = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Hash the password
    hashed_password = password_hash.hash(user.password)

    # Create new user
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    # Save user to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Account created successfully",
        "user_id": new_user.id
    }



@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    # Find user by username
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    # User not found
    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    # Check password
    password_is_correct = password_hash.verify(
        user.password,
        existing_user.password
    )

    # Wrong password
    if not password_is_correct:
        raise HTTPException(
            status_code=401,
            detail="Wrong password"
        )

    return {
        "message": "Login successful",
        "user_id": existing_user.id,
        "username": existing_user.username
    }