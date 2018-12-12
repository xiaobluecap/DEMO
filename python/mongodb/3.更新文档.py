from pymongo import MongoClient

#连接服务器

conn=MongoClient("localhost",27017)


#连接数据库
db=conn.python

#获取集合

collection=db.student


#更新文档
collection.update({"name":"lilei"},{"$set":{"age":25}})


#断开连接
conn.close()