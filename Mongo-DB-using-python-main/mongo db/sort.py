import pymongo

myclient = pymongo.MongoClient("db")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")
"""mydoc = mycol.find().sort("name",-1) -decending"""


for x in mydoc:
  print("sort by name ",x)
