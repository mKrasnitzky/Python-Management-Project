import fastapi
from app.db_management import expensesIncome_CRUD

expensesIncome_router = fastapi.APIRouter()


@expensesIncome_router.get('/all')
async def get():
    return await expensesIncome_CRUD.get_all()


@expensesIncome_router.post('/')
async def post():
    return await expensesIncome_CRUD.get_all()
