from app.db_management.config_db import expensesAndIncomeCollection
from app.models.Expenses_incomes import Expenses_Income


async def get_all():
    x = list(expensesAndIncomeCollection.find())
    [s.pop('_id') for s in x]
    return x
    # return [Expenses_Income(**expenses_income) for expenses_income in Expenses_Income.find()]


async def get(id: int):
    expensesAndIncomeCollection.find({
        "id": id
    })


async def add_expenses(list: Expenses_Income):
    expensesAndIncomeCollection.insert_one(list.dict)
    return 1


async def update(id: int, name: String):
    expensesAndIncomeCollection.insert_one({
        "id": id,
        "name": name
    })


async def delete(ei: Expenses_Income):
    expensesAndIncomeCollection.delete_one(ei)
    return "the object delete"

