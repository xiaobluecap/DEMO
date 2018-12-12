from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId#用于id查询

#连接服务器

conn=MongoClient("localhost",27017)


#连接数据库
db=conn.python

#获取集合

collection=db.student


#查询文档

#查询部分文档
'''
res=collection.find({"age":{"$gt":18}})
for roe in res:
    print(roe)
'''

#查询所有文档
'''res=collection.find()
for roe in res:
    print(roe)
'''

#统计查询
'''
res=collection.find({"age":{"$gt":18}}).count()
print(res)
'''
#根据id查询
'''
res=collection.find({"_id":ObjectId("5b0ad025f38538489824c3f6")})
print(res[0])
'''
#排序
'''
#res=collection.find().sort("age")#升序
res=collection.find().sort("age",pymongo.DESCENDING)#降序
for roe in res:
    print(roe)
'''
#分页
res=collection.find().skip(3).limit(2)
for roe in res:
    print(roe)





#断开连接
conn.close()