# a=lambda a,b,c: a+b+c
# print(a(5,4,3))

# a=lambda name:name*5
# print(a('balu'))


# l1=[12,22,32,42,25]
# l2=[]
# for i in l1:
#     t=lambda a : a+1
#     l2.append(t(i))
# print(l2)

# filter
# Syntax
# filter(function,sequence)
# balu=[1,2,3,4,5,6]
# def myfunc(x):
#   if x>=6:
#     return True
#   else:
#     return False 
# ball=filter(myfunc, balu)
# print(list(ball))

# map
# syntax
# def balu(n):
#     return n**2
# numbers =(1,2,3,4)
# result =map(balu,numbers)
# print(list(result))

# generator function 
# def function():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# x=function()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# def function():
#     return 1
#     return 2
# x=function()
# print(x.__next__())

# reduce 
# syntax
# from functools import reduce
# a=reduce(lambda a,b,:a+b,[1,2,3,4])
# print(a)


