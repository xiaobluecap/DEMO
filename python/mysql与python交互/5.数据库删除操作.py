import pymysql
db=pymysql.connect("localhost","root","root","python")
cursor=db.cursor()


sql='delete from student where name="tony"'
try:
    cursor.execute(sql)
    db.commit()
except:
    #如果提交失败，回滚到上一次
    db.rollback()

cursor.close()
db.close()