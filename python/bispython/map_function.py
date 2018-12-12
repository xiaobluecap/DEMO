'''
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
def f(x):
    return x*x*x

r=map(f,[1,2,3,4,5,6])
print(r)
# <map object at 0x00000207D1DA5F28>
print(list(r))



def normalize(str):
    return str.lower().title()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)