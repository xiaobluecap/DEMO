guiyuan1020s=['hashiqi','faming','piaochang','pangzi']
for guiyuan1020 in guiyuan1020s:      #遍历guiyuan1020列表并在每个人后面输出语句
    print("the best handsome people is\t"+guiyuan1020.title())
print(guiyuan1020s[0].title()+":I'm a dog")#最后输出语句
b=[]
for key in range(1,6,2): #遍历key列表
    print(key)
    a=key**3            #a的三次方
    b.append(a)         #赋值给b
print(b)
print([c**3 for c in range(1,6,2)])
print(min(b))      #最小
print(max(b))      #最大
print(sum(b))      #求和
print(b[:-2])      #输出b列表从0到倒数第二位元素但不包括倒数第二位元素
for guiyuan1020 in guiyuan1020s[:-1]:
    print(guiyuan1020)
d=guiyuan1020s[:] #复制guiyuan1020s
print(d)
guiyuan1020s.append('vip') #检查guiyuan1020s和d是不是两个列表
d.append('zj')
print(guiyuan1020s)
print(d)
e=('hashiqi','faming','piaochang','pangzi')
print(e[0])   #输出指定列表元素
print('hashiqi' in guiyuan1020s) #判断一个元素是否在列表里