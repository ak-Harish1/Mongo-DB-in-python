import pymongo

myclient = pymongo.MongoClient("db")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "name": {"$regex": "^J"} }
'''delete many documents'''
x = mycol.delete_many(myquery)
'''x = mycol.delete_many({})  delete all documents'''

print(x.deleted_count, " documents deleted.")
