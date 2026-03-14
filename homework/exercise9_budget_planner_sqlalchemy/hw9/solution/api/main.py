from fastapi import FastAPI
from solution.api.routers import (
    accounts,
    categories,
    reports,
    transactions,
    transfers,
)

app = FastAPI()

app.include_router(accounts.router)
app.include_router(categories.router)
app.include_router(transactions.router)
app.include_router(transfers.router)
app.include_router(reports.router)


# uvicorn solution.api.main:app --reload
