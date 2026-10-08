from fastapi import FastAPI

from database import Base, engine
from routers import auth
from routers import account
from routers import expense
from routers import dashboard

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="Finance Tracker API",
    description="Expense and Financial Analysis API",
    version="1.0.0"
)

# Register routers
app.include_router(auth.router)
app.include_router(account.router)
app.include_router(expense.router)
app.include_router(dashboard.router)

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Finance Tracker API is running"
    }