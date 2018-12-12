
import pymysql

db=pymysql.connect("localhost","root","root","python")
cursor=db.cursor()
#检查表是否存在，如果存在则删除
cursor.execute("drop table if EXISTS bandcards")
#建表
sql="create table bandcards(id int auto-increment primary key,money int not null)"
cursor.execute(sql)
cursor.close()
db.close()