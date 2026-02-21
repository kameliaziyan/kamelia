from dataclasses import dataclass
from fastapi import FastAPI
from solution.budget_hw4 import Budget

#run :
#fastapi dev ./solution/budget_planner_api.py

INCOME = "income"
EXPENSE = "expense"

app = FastAPI()
budget_manager = Budget()



@dataclass
class IncomeRequest:
    amount: float
    description: str


@dataclass
class ExpenseRequest:
    amount: float
    description: str



@app.post("/income")
async def create_income(income_data: IncomeRequest) -> dict:
    budget_manager.add(income_data.description, income_data.amount, INCOME)

    return {
        "message": "Income created successfully",
        "details": {
            "amount": income_data.amount,
            "description": income_data.description,
        },
    }


@app.post("/expense")
async def create_expense(expense_data: ExpenseRequest) -> dict:
    budget_manager.add(expense_data.description, expense_data.amount, EXPENSE)

    return {
        "message": "Expense created successfully",
        "details": {
            "amount": expense_data.amount,
            "description": expense_data.description,
        },
    }



@app.delete("/income/{income_id}")
async def remove_income(income_id: int) -> dict:
    for income in budget_manager.incomes:
        if income.id == income_id:
            removed_income = income
            break
    else:
        return {"message": "Income not found"}

    budget_manager.remove(income_id, INCOME)

    return {
        "message": "Income removed successfully",
        "details": {
            "id": removed_income.id,
            "description": removed_income.description,
            "amount": removed_income.amount,
        },
    }


@app.delete("/expense/{expense_id}")
async def remove_expense(expense_id: int) -> dict:
    for expense in budget_manager.expenses:
        if expense.id == expense_id:
            removed_expense = expense
            break
    else:
        return {"message": "Expense not found"}

    budget_manager.remove(expense_id, EXPENSE)

    return {
        "message": "Expense removed successfully",
        "details": {
            "id": removed_expense.id,
            "description": removed_expense.description,
            "amount": removed_expense.amount,
        },
    }



@app.get("/income")
async def list_incomes() -> dict:
    return {
        "message": "Income list retrieved",
        "data": [
            {
                "id": income.id,
                "description": income.description,
                "amount": income.amount,
            }
            for income in budget_manager.incomes
        ],
    }


@app.get("/expense")
async def list_expenses() -> dict:
    return {
        "message": "Expense list retrieved",
        "data": [
            {
                "id": expense.id,
                "description": expense.description,
                "amount": expense.amount,
            }
            for expense in budget_manager.expenses
        ],
    }


@app.get("/summary")
async def get_summary() -> dict:
    return {
        "message": "Summary retrieved",
        "data": budget_manager.summary(),
    }


@app.delete("/clear")
async def clear_budget() -> dict:
    budget_manager.clear_all()
    return {"message": "All records cleared successfully"}