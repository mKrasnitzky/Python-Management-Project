import pymongo

Client = pymongo.MongoClient("mongodb://localhost:27017/")
db = Client["management_database"]
expensesAndIncomeCollection = db["ExpensesAndIncomes-collection"]
usersCollection = db["Users-collection"]

expensesAndIncomesList = [
    {"sum": 5000, "name": "salary", "expensesOrIncome": "expenses"},
    {"sum": 250, "name": "shopping", "expensesOrIncome": "income"}
]

usersCollectionList = [
    {"_id": 0, "userName": "MosheGilad", "password": "123456", "firstName": "Moshe", "lastName": "Gilad",
     "city": "Jerusalem", "phoneNumber": "050-7637637"},
    {"_id": 1, "userName": "ab", "password": "12", "firstName": "a", "lastName": "b", "city": "Bat Yam",
     "phoneNumber": "053-1111111"},
]

# expensesAndIncomeCollection.insert_many(expensesAndIncomesList)
# usersCollection.insert_many(usersCollectionList)
