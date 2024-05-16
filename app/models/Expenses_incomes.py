from pydantic import BaseModel
import ExpensesOrIncome


class Expenses_Income(BaseModel):
    id: int
    sum: int
    name: str
    expensesOrIncome: ExpensesOrIncome
