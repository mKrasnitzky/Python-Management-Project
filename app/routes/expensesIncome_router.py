import fastapi
from app.db_management import expensesIncome_CRUD

expensesIncome_router = fastapi.APIRouter()


@expensesIncome_router.get('/all')
async def get():
    print("in func get")
    return await expensesIncome_CRUD.get_all()


@expensesIncome_router.get('/{id}')
async def get(id: int):
    return await expensesIncome_CRUD.get(id)


@expensesIncome_router.post('/')
async def post():
    return await expensesIncome_CRUD.get_all()


@expensesIncome_router.put('/{id}/{name}')
async def put():
    return await expensesIncome_CRUD.updata(id, name)


@expensesIncome_router.delete('/delete', response_model=Expenses_Income)
async def delete(expenses_income: Expenses_Income):
    return await expensesIncome_CRUD.delete(expenses_income)
