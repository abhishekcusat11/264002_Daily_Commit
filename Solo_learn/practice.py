# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])


# while False:
#   print("Looping...")


# def print_double(x):
#        print(2 * x)

# print_double(3)

# test = { }
# print(test[0])


# fib = {1: 1, 2: 1, 3: 2, 4: 3}
# print(fib.get(4, 0) + fib.get(7, 5))
# print("{0}{1}{0}".format("abra", "cad"))
# str="{c}, {b}, {a}".format(a=5, b=9, c=7)
# print(str)

# a=min([sum([11, 22]), max(abs(-30), 2)])
# print(a)

# nums = [-1, 2, -3, 4, -5]
# if all([abs(i) < 3 for i in nums]):
#   print(1)
# else:
#   print(2)

# nums = (55, 44, 33, 22)
# print(max(min(nums[:2]), abs(-42)))

# def test(func, arg):
#       return func(func(arg))

# def mult(x):
#   return x * x

# print(test(mult, 2))

# def func(x):
#       y = x**2
#   z = x + y
#   return z

# def fib(x):
#       if x == 0 or x == 1:
#         return 1
#       else: 
#         return fib(x-1) + fib(x-2)
# print(fib(4))

# a = {1, 2, 3}
# b = {0, 3, 4, 5}
# print(a & b)

# There are many functions in itertools that operate on iterables, in a similar way to map and filter.
# Some examples:
# takewhile - takes items from an iterable while a predicate function remains true;
# chain - combines several iterables into one long one;
# accumulate - returns a running total of values in an iterable.
# from itertools import product
# a={1, 2}
# print(len(list(product(range(3), a))))

# 

# def power(x, y):

#     if y == 0:

#         return 1
#     else:
#         return x * power(x, y-1)		
# print(power(2, 3))
# # 
# def func(**kwargs):
#     print(kwargs["zero"])

# func(a = 0, zero = 8)
# for i in range(10):
#     try: 
#         if 10 / i == 2.0:
#             break
#         except ZeroDivisionError:
# #             print(1)
# #         else:
# #             print(2)

# i=0
# while i<=5:
#     i+=1
#     if i%2 ==0:
#         break
#     print("*")

# x=1
# x=x==x
# print(x)

# l1=[1,2,3]
# l2=[]
# for v in l1:
#     l2.insert(0,v)
# print(l2)

# z=10
# y=0
# x=y<z and z>y or y>z and z<y
# print(x)

# a=1
# b=0
# c=a&b
# d=a|b 
# e=a^b
# print(c+d+e)
# t= [[3-i for i in range(3)] for j in range(3) ]
# s=0
# for i in range(3):
#     s+=t[i][i]
# print(s)

# nums =[1,2,3]
# vals=nums[-1:-2]
# print(vals)
# print(nums)
# def func_1(a):
#     return a**a 
# def func_2(a):
#     return func_1(a) * func_2(a)
# print(func_2(2))
# import math
# result=math.e !=math.pow(2,4)
# print(int(result))
# 
# from random import randint
# for i in range(2):
#     print(randint(1,2) ,end='')
# x='\''
# # print(len(x))
# try:
#     print("5"/0)
# except ArithmeticError:
#     print("Arith")
# except ZeroDivisionError:
#     print("Zero")
# except:
#     print("some")