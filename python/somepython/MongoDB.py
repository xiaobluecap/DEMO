import pymongo

conn=pymongo.MongoClient(host='localhost',port=27017)

db=conn.pacong

collection=db.some

collection.insert({"name":"456","age":20,"gender":1,"address":"上海","isdelete":0})


conn.close()


