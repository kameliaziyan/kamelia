from fastapi import FastAPI
from solution.budget_hw4 import Budget

# fastapi dev ./solution/budget_planner_api.py

INCOME = "income"
EXPENSE = "expense"

app = FastAPI()
planner = Budget()


@app.post("/income")
async def add_income(description: str, amount: float) -> dict:
    planner.add(description, amount, INCOME)
    return {"message": "Income added successfully"}


@app.post("/expense")
async def add_expense(description: str, amount: float) -> dict:
    planner.add(description, amount, EXPENSE)
    return {"message": "Expense added successfully"}


@app.delete("/income/{item_id}")
async def delete_income(item_id: int) -> dict:
    planner.remove(item_id, INCOME)
    return {"message": "Income deleted successfully"}


@app.delete("/expense/{item_id}")
async def delete_expense(item_id: int) -> dict:
    planner.remove(item_id, EXPENSE)
    return {"message": "Expense deleted successfully"}


@app.get("/income")
async def get_income() -> list[dict]:
    return [
        {
            "id": income.id,
            "description": income.description,
            "amount": income.amount,
        }
        for income in planner.incomes
    ]


@app.get("/expense")
async def get_expense() -> list[dict]:
    return [
        {
            "id": expense.id,
            "description": expense.description,
            "amount": expense.amount,
        }
        for expense in planner.expenses
    ]


@app.get("/summary")
async def summary() -> dict:
    return planner.summary()


@app.delete("/clear")
async def clear_all() -> dict:
    planner.clear_all()
    return {"message": "All data cleared successfully"}
