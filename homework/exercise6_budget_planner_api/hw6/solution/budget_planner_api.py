from dataclasses import dataclass
from fastapi import FastAPI
from solution.budget_hw4 import Budget

# run :
# fastapi dev ./solution/budget_planner_api.py

INCOME = "income"
EXPENSE = "expense"
KEY_MESSAGE = "message"
KEY_DETAILS = "details"
KEY_AMOUNT = "amount"
KEY_DESCRIPTION = "description"
KEY_ID = "id"

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
        KEY_MESSAGE: "Income created successfully",
        KEY_DETAILS: {
            KEY_AMOUNT: income_data.amount,
            KEY_DESCRIPTION: income_data.description,
        },
    }


@app.post("/expense")
async def create_expense(expense_data: ExpenseRequest) -> dict:
    budget_manager.add(expense_data.description, expense_data.amount, EXPENSE)

    return {
        KEY_MESSAGE: "Expense created successfully",
        KEY_DETAILS: {
            KEY_AMOUNT: expense_data.amount,
            KEY_DESCRIPTION: expense_data.description,
        },
    }


@app.delete("/income/{income_id}")
async def remove_income(income_id: int) -> dict:
    for income in budget_manager.incomes:
        if income.id == income_id:
            removed_income = income
            break
    else:
        return {KEY_MESSAGE: "Income not found"}

    budget_manager.remove(income_id, INCOME)

    return {
        KEY_MESSAGE: "Income removed successfully",
        KEY_DETAILS: {
            KEY_ID: removed_income.id,
            KEY_DESCRIPTION: removed_income.description,
            KEY_AMOUNT: removed_income.amount,
        },
    }


@app.delete("/expense/{expense_id}")
async def remove_expense(expense_id: int) -> dict:
    for expense in budget_manager.expenses:
        if expense.id == expense_id:
            removed_expense = expense
            break
    else:
        return {KEY_MESSAGE: "Expense not found"}

    budget_manager.remove(expense_id, EXPENSE)

    return {
        KEY_MESSAGE: "Expense removed successfully",
        KEY_DETAILS: {
            KEY_ID: removed_expense.id,
            KEY_DESCRIPTION: removed_expense.description,
            KEY_AMOUNT: removed_expense.amount,
        },
    }


@app.get("/income")
async def list_incomes() -> dict:
    return {
        KEY_MESSAGE: "Income list retrieved",
        "data": [
            {
                KEY_ID: income.id,
                KEY_DESCRIPTION: income.description,
                KEY_AMOUNT: income.amount,
            }
            for income in budget_manager.incomes
        ],
    }


@app.get("/expense")
async def list_expenses() -> dict:
    return {
        KEY_MESSAGE: "Expense list retrieved",
        "data": [
            {
                KEY_ID: expense.id,
                KEY_DESCRIPTION: expense.description,
                KEY_AMOUNT: expense.amount,
            }
            for expense in budget_manager.expenses
        ],
    }


@app.get("/summary")
async def get_summary() -> dict:
    return {
        KEY_MESSAGE: "Summary retrieved",
        "data": budget_manager.summary(),
    }


@app.delete("/clear")
async def clear_budget() -> dict:
    budget_manager.clear_all()
    return {KEY_MESSAGE: "All records cleared successfully"}
