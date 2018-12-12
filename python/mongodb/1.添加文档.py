from pymongo import MongoClient

#连接服务器

conn=MongoClient("localhost",27017)


#连接数据库
db=conn.somepython

#获取集合

collection=db.study


#添加文档
collection.insert({"name":"456","age":20,"gender":1,"address":"上海","isdelete":0})


#断开连接
conn.close()