from fastapi import FastAPI
from exercise4_budget_planner.hw4.solution.budget import BudgetPlanner
from homework.exercise4_budget_planner.hw4.solution import budget


INCOME = "income"
EXPENSE = "expense"

app = FastAPI()

planner = BudgetPlanner()   

@app.post("/income")
def add_income(data: dict):
    budget.add(data["description"], data["amount"], INCOME)
    return {"message": "Income added successfully"}


