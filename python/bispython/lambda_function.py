'''
lambda [arg1 [, agr2,.....argn]] : expression
# 1、单个参数的：
# >>> g = lambda x : x ** 2
# >>> print g(3)
# 9
# 2、多个参数的：
# >>> g = lambda x, y, z : (x + y) ** z
# >>> print g(1,2,2)
# 9

可以直接作为list和dict的成员
'''

list_a=[lambda a:a*a,lambda b:b*b*b]
print(list_a[0])
g=list_a[0]
print(g)
print(g(8))