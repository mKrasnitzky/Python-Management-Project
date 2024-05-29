from app.db_management.config_db import expensesAndIncomeCollection
from app.models.Expenses_incomes import Expenses_Income


async def get_all():
    print("befor הקריאה לDB")
    x = list(expensesAndIncomeCollection.find())
    [s.pop('_id') for s in x]
    print("in func get_all")
    return x
    # return [Expenses_Income(**expenses_income) for expenses_income in Expenses_Income.find()]


async def add_expenses(list: Expenses_Income):
    expensesAndIncomeCollection.insert_one(list.dict)
    return 1
# async  def update(expenses_Income: Expenses_Income):
#
