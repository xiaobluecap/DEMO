# # A simple generator function
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n
#
#     n += 1
#     print('This is printed second')
#     yield n
#
#     n += 1
#     print('This is printed at last')
#     yield n
#
#
# # a=my_gen()
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
#
# for iter in my_gen():
#     print(iter)



# a=(x for x in range(9))
# for item in a:
#     print(item)

# class PowTwo:
#     def __init__(self, max=0):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n > self.max:
#             raise StopIteration
#
#         result = 2 ** self.n
#         self.n += 1
#         return result

#
# def PowTwoGen(max = 0):
#     n = 0
#     while n < max:
#         yield 2 ** n
#         n += 1
#
#
# p=PowTwoGen()
# for item in p(6):
#     print(item)

# import sys
# a=sys.argv[0]
# print(a)




# import bisect,sys
# HAYSTACK=[1,4,5,6,8,12,15,20,21,23,23,26,29,30]
# NEEDLES=[0,1,2,5,8,10,22,23,29,30,31]
# ROW_FMT='{0:2d}@{1:2d} {2}{0:<2d}'
# def demo(bisect_fn):
#     for needle in reversed(NEEDLES):
#         position = bisect_fn(HAYSTACK,needle)
#         offset = position * '  |'
#         print(ROW_FMT.format(needle,position,offset))
#
# if __name__=='__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect_left
#     print('DEMO:',bisect_fn.__name__)
#     print('haystack ->',' '.join('%2d'%n for n in HAYSTACK))
#     demo(bisect_fn)

# import random
# list=[random.randint(0,100) for _ in range(100)]
# print(list)



# import bisect
# import random
#
# random.seed(1)
#
# random.seed(1)
#
# print('New  Pos Contents')
#
# print('---  --- --------')
#
# l = []
# for i in range(1, 15):
#     r = random.randint(1, 100)
#     position = bisect.bisect(l, r)
#     bisect.insort(l, r)
#     print('%3d  %3d' % (r, position), l)

# import bisect
#
# list=[1,2,3,4,5,6,7,8,9]
# a=5
# position=bisect.bisect_left(list,a)
# print(position)
# print(list)
import numpy

















