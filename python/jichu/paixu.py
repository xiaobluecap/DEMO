A=['shanliang','qinfen','dafang']   #列表元素的删除与增添
print(A)
A.sort()             #使用sort函数倒序排列
print(A)
A.sort(reverse=False)#使用sort函数正序排列
print(A)
print(len(A))        #使用len函数判断列表长度
del A[2]             #使用del函数永久删除任意位置的元素
print(A)
a=A.pop()            #使用pop函数永久删除末尾位置的元素
print(A)
print(a)
A.insert(1,'qinfen') #使用insert函数增添任意位置的元素
print(A)
A.append('dafang')   #使用append函数增加末尾位置的元素
print(A)
b=A.remove(A[0])     #使用remov函数删除指定位置的元素（但可继续使用）
print(A)