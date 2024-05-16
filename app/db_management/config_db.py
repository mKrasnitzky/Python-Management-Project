import pymongo

Client = pymongo.MongoClient("mongodb://localhost:27017/")
db = Client["management_database"]
expensesAndIncomeCollection = db["ExpensesAndIncomes-collection"]

mylist = [
  {"_id": 0, "sum": 5000, "name": "salary", "expensesOrIncome": "expenses"},
  {"_id": 1, "sum": 250, "name": "shopping", "expensesOrIncome": "income" }
]

x = expensesAndIncomeCollection.insert_many(mylist)

print(x.inserted_ids)
