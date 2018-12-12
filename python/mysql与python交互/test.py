from  Pmysql import pMysql

s=pMysql("localhost","root","root","python")

res=s.get_all("select * from student where id>2")
for row in res:
    print(res)

