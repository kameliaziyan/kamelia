from fastapi import FastAPI
from solution.budget_hw4 import Budget



INCOME = "income"
EXPENSE = "expense"

app = FastAPI()
planner = Budget()   


@app.post("/income")
async def add_income(description : str, amount : float):
    planner.add(description, amount, INCOME)
    return {"message": "Income added successfully"}


@app.post("/expense")
async def add_income(description : str, amount : float):
    planner.add(description, amount, EXPENSE)
    return {"message": "expense added successfully"}

@app.delete("/income_/{description}")
async def delete_income(description: str):
    planner.remove(description , INCOME)
    return{"message": "Income deleted successfully"}

@app.delete("/expense_/{description}")
async def delete_expense(description: str):
    planner.remove(description , EXPENSE)
    return{"message": "expense deleted successfully"}

@app.get("/summary")
async def summary():
    return (planner.summary())

@app.delete("/clear")
async def clear_all():
    return (planner.clear_all())


    


