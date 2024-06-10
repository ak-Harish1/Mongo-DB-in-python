import pymongo

myclient = pymongo.MongoClient("db")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myresult = mycol.find().limit(3)

#print the result:
for x in myresult:
  print(x)
