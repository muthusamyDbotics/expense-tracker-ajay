from fastapi import FastAPI

from database import Base, engine

from routers import auth
from routers import account
from routers import expense
from routers import dashboard



Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(auth.router)
app.include_router(account.router)
app.include_router(expense.router)
app.include_router(dashboard.router)


@app.get("/")
def home():

    return {
        "message": "Finance Tracker API is running"
    }