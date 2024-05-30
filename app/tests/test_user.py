import pytest
from app.db_management import user_CRUD
from app.models.LoginRequest import LoginRequest
from app.models.User import User


@pytest.mark.parametrize("user", [
    User(id=0, userName="hhh", password="ffff=.n<3&~IsHm}", firstName="QVcrNT", lastName="xezTsUtTocnbamCJN",
         city="LEmDIxRytPtH FUYYRfAeRrnFriaaCIkxokLfQdEWOgHFZcFUb", phoneNumber="731183773299661")])
@pytest.mark.asyncio
async def test_register(user):
    res = await user_CRUD.login(user)
    expect_id = await user_CRUD.set_id()
    print(expect_id)
    print(res)
    assert res is not None
    # assert res


@pytest.mark.parametrize("login_request", [LoginRequest(userName="aaa", password="ffff=.n<3&~IsHm}")])
@pytest.mark.asyncio
async def test_login(login_request):
    res = await user_CRUD.login(login_request)
    print(res)
    assert res is not  None


@pytest.mark.parametrize("user", [User(id=8,
                                       userName="aaa",
                                       password="ffff=.n<3&~IsHm}",
                                       firstName="jj",
                                       lastName="xezTsUtTocnbamCJN",
                                       city="LEmDIxRytPtH FUYYRfAeRrnFriaaCIkxokLfQdEWOgHFZcFUb",
                                       phoneNumber="731183773299661")])
@pytest.mark.asyncio
async def test_update_user(user):
    res = await user_CRUD.update_user("aaa", user)
    assert res is not  None

