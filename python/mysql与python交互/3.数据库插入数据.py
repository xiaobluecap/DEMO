import pymysql
db=pymysql.connect("localhost","root","root","python")
cursor=db.cursor()


sql='insert into student values(0,"ojd",1,2)'
try:
    cursor.execute(sql)
    db.commit()
except:
    #如果提交失败，回滚到上一次
    db.rollback()

cursor.close()
db.close()