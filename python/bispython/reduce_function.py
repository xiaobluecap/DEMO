'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
from functools import reduce
def add(x,y):
    return x+y
r=reduce(add,[1,2,3,4,5,6])
print(r)
def fn(x,y):
    return x*10+y
q=reduce(fn,[4,5,6,7,8,9])
print(q)
def char2Int(s):
    digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
w=reduce(fn,map(char2Int,'123456'))
print(w)

'''
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
'''
def prod(L):
    def ss(s):
        return s*s*s
    return reduce(sum,map(ss,L))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
# list_q=map(ss,[1,2,3,4,5])
# print(list(list_q))