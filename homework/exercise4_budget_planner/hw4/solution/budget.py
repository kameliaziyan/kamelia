# Business logic (classes for Budget, Income, Expense)



class Income():
    description : str
    amount : float
    def __init__(self, description,amount ):
        self.description = description
        self.amount = amount




class Expense():
     description : str
     amount : float
     def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        


class Budget():
    
    def __init__(self):
        self._incomes = []
        self._expenses = []

    def add_income(self, description: str, amount: float) -> None:
        income = Income(description,amount)
        self._incomes.append(income)

    def add_expense(self, description: str, amount: float) -> None:
        expenses = Expense(description,amount)
        self._expenses.append(expenses)

    def total_income(self) -> float:
        total = 0
        for income in self._incomes :
            total += income.amount
        return total

    def total_expense(self) -> float:
        total = 0
        for expense in self._expenses:
            total += expense.amount
        return total
        

    def remaining_budget(self) -> float:
        remaining = self.total_income() - self.total_expense()
        return remaining
    
    def remove_income(self) :
        pass

    def remove_expense(self):
        pass

    def clear_all(self):
        pass


        
        




    