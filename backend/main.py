
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base

# Import models so SQLAlchemy can create the tables
import models

# Import routers
from routers import auth
from routers import account
from routers import expense
from routers import dashboard


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Finance Tracker API",
    description="Expense and Financial Analysis API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    auth.router
)

app.include_router(
    account.router
)

app.include_router(
    expense.router
)

app.include_router(
    dashboard.router
)


@app.get("/")
def home():

    return {
        "message": "Finance Tracker API is running"
    }
