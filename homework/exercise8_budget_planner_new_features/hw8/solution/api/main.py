from fastapi import FastAPI

from hw8.solution.api.routers import (
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


# python3 -m solution.main
