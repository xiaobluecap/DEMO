# test=type('Test',(object,),{'name':None})
# test

mylist = [1,2,2,2,2,3,3,3,4,4,4,4]
myset = set(mylist)  #myset是另外一个列表，里面的内容是mylist里面的无重复 项
for item in myset:
    print("the %d has found %d" %(item,mylist.count(item)))
