import pymysql
'''
#链接数据库
#参数
localhost mysql服务所在主机
root 用户名
root 密码
python 要连接的数据库名
'''
#db=pymysql.connect("localhost","root","root","python")
db=pymysql.connect("169.254.119.163","root","root","python")


#创建cursor对象
cursor=db.cursor()


sql="select version()"

#执行sql语句
cursor.execute(sql)


#获取返回的信息
data=cursor.fetchone()

print(data)


#断开
cursor.close()
db.close()