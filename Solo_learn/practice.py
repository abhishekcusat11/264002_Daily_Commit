# # list = [1, 1, 2, 3, 5, 8, 13]
# # print(list[list[4]])


# # while False:
# #   print("Looping...")


# # def print_double(x):
# #        print(2 * x)

# # print_double(3)

# # test = { }
# # print(test[0])


# # fib = {1: 1, 2: 1, 3: 2, 4: 3}
# # print(fib.get(4, 0) + fib.get(7, 5))
# # print("{0}{1}{0}".format("abra", "cad"))
# # str="{c}, {b}, {a}".format(a=5, b=9, c=7)
# # print(str)

# # a=min([sum([11, 22]), max(abs(-30), 2)])
# # print(a)

# # nums = [-1, 2, -3, 4, -5]
# # if all([abs(i) < 3 for i in nums]):
# #   print(1)
# # else:
# #   print(2)

# # nums = (55, 44, 33, 22)
# # print(max(min(nums[:2]), abs(-42)))

# # def test(func, arg):
# #       return func(func(arg))

# # def mult(x):
# #   return x * x

# # print(test(mult, 2))

# # def func(x):
# #       y = x**2
# #   z = x + y
# #   return z

# # def fib(x):
# #       if x == 0 or x == 1:
# #         return 1
# #       else: 
# #         return fib(x-1) + fib(x-2)
# # print(fib(4))

# # a = {1, 2, 3}
# # b = {0, 3, 4, 5}
# # print(a & b)

# # There are many functions in itertools that operate on iterables, in a similar way to map and filter.
# # Some examples:
# # takewhile - takes items from an iterable while a predicate function remains true;
# # chain - combines several iterables into one long one;
# # accumulate - returns a running total of values in an iterable.
# # from itertools import product
# # a={1, 2}
# # print(len(list(product(range(3), a))))

# # 

# # def power(x, y):

# #     if y == 0:

# #         return 1
# #     else:
# #         return x * power(x, y-1)		
# # print(power(2, 3))
# # # 
# # def func(**kwargs):
# #     print(kwargs["zero"])

# # func(a = 0, zero = 8)
# # for i in range(10):
# #     try: 
# #         if 10 / i == 2.0:
# #             break
# #         except ZeroDivisionError:
# # #             print(1)
# # #         else:
# # #             print(2)

# # i=0
# # while i<=5:
# #     i+=1
# #     if i%2 ==0:
# #         break
# #     print("*")

# # x=1
# # x=x==x
# # print(x)

# # l1=[1,2,3]
# # l2=[]
# # for v in l1:
# #     l2.insert(0,v)
# # print(l2)

# # z=10
# # y=0
# # x=y<z and z>y or y>z and z<y
# # print(x)

# # a=1
# # b=0
# # c=a&b
# # d=a|b 
# # e=a^b
# # print(c+d+e)
# # t= [[3-i for i in range(3)] for j in range(3) ]
# # s=0
# # for i in range(3):
# #     s+=t[i][i]
# # print(s)

# # nums =[1,2,3]
# # vals=nums[-1:-2]
# # print(vals)
# # print(nums)
# # def func_1(a):
# #     return a**a 
# # def func_2(a):
# #     return func_1(a) * func_2(a)
# # print(func_2(2))
# # import math
# # result=math.e !=math.pow(2,4)
# # print(int(result))
# # 
# # from random import randint
# # for i in range(2):
# #     print(randint(1,2) ,end='')
# # x='\''
# # # print(len(x))
# # try:
# #     print("5"/0)
# # except ArithmeticError:
# #     print("Arith")
# # except ZeroDivisionError:
# #     print("Zero")
# # except:
# #     print("some")
# # print('Milk' >"Milkey")
# # 
# # class A:
# #     def __init__(self,v=1):
# #         self.v=v
# #     def set(self ,v):
# #         self.v=v
# #         return v
# # a=A()
# # print(a.set(a.v+1))
# # class A:
# #     def __str__(self):
# #         return 'a'
# # class B:
# #     def __str__(self):
# #         return 'b'
# # class C(A,B):
# #     pass
# # o = C()
# # print(o)


# # class A:
# #     pass
# # class B(A):
# #     pass
# # class C(B):
# #     pass
# # print(issubclass(C,A))
# # class A:
# #         def __init__(self):
# #             self.a=1
# # class B(A):
# #         def __init__(self):
# #             self.b=2
# # l=[0,1,2,3,4,5,6]
# # foo=tuple(filter(lambda x:x-0 and x-1 ,l))
# # print(foo)
# # b=bytearray(3)
# # print(b)
# # import calendar
# # print(calendar.weekheader(2))
# # from datetime import date
# # date_1=date(1992,1,16)
# # date2=date(1991,2,5)
# # print(date_1-date2)
# # from datetime import datetime
# # datetime=datetime(2019 ,11,27,11,27,22)
# # print(datetime.strftime('%Y/%B/%d%H:%M:%S'))
# # def fun(n):
# #     s='+'
# #     for i in range(n):
# #         s+=s
# #         yield s

# # for x in fun(2):
# #     print(x,end='')
# # import os
# # os.mkdir('thumbnails')
# # os.chdir('thumbnails')
# # sizes=['small' ,'medium' ,'large']
# # for size in sizes:
# #     os.mkdir(size)
# # print(os.listdir())
# # def o(p):
# #     def q():
# #         return '*' * p
# #     return q
# # r=o(1)
# # s=o(2)
# # print(r() + s())
# # import os
# # os.mkdir('pictures')
# # os.chdir('pictures')
# # os.mkdir('thumbnails')
# # os.chdir('thumbnails')
# # os.mkdir('tmp')
# # os.chdir('../')
# # print(os.getcwd())

# # import calendar
# # c=calendar.Calendar()
# # for weekday in c.iterweekdays():
# #     print(weekday ,end= " ")

# # def I():
# #     s='abcdef'
# #     for c in s[::2]:
# #         yield c
# # for x in I():
# #     print(x,end='')
# # class A:
# #     def __init__(self, v=2):
# #         self.v=v
# #     def set(self ,v=1):
# #         self.v +=v
# #         return self.v
# # a=A()
# # b=a 
# # b.set()
# # print(a.v)
# # import calendar
# # calendar.setfirstweekday(calendar.SUNDAY)
# # print(calendar.weekheader(3))
# # print(float("1.3"))
# # import os
# # os.mkdir('new')
# # os.chdir('new')
# # print(os.getcwd)
# # from datetime import datetime
# # date1=datetime(2019 , 11, 27,11,27,22)
# # date2=datetime(2019,11,27,0,0,0)
# # print(date1-date2)4
# # x="\\\\"
# # print(len(x))
# # try:
# #     raise Exception
# # except:
# #     print("c")

# # except BaseException:
# #     print("a")

# # except Exception:
# #     print("b")
# # x="\\\"
# # print(len(x))

# # import random
# # a=random.randrange(10,100,3)
# # b=random.randint(0,100)  
# # c=random.choice((0,100,3)) 
# # print(__name__)
# # # print(a , b, c)
# # try:
# #     raise Exception(1,2,3)
# # except Exception as e:
# #     print(len(e.args))
# # n=[0,2,7,9,10]
# # foo=map(lambda num: num**2 ,n)
# # print(list(foo))

# # class A:
# #     A=1
# #     def __init__(self):
# #         self.a=0;
# # print(hasattr(A, 'a'))

# # from datetime import timedelta
# # delta=timedelta(weeks=1 ,days=7 ,hours=11)
# # print(delta*2)
# # n=[i*i for i in range(5)]
# # foo=list(filter(lambda num: num%2 ,n))
# # print(foo)
# # class A:
# #     pass
# # class B(A):
# #     pass
# # class C(B):
# #     pass
# # print(issubclass(A,C))
# # import os 
# # os.mkdir('pictures')
# # os.chdir('pictures')
# # print(os.getcwd)
# # s1='Bond'
# # s2='James Bond'
# # print(s1.isalpha() ,s2.isalpha())
# # class A:

# #     def __init__(self):

# #         pass
    

# #     def f(self):
# #         return 1
    
# #     def g():
# #         return self.f()

# # a=A()
# # # print(a.g())

# # import os
# # os.makedirs('pic/thu')
# # # os.rmdir('pic')

# # # import calendar
# # # c=calendar.Calendar(calendar.SUNDAY)
# # # for weekday in c.iterweekdays():
# # from datetime import timedelta
# # delta =timedelta(weeks=1 ,days= 7, hours=11)
# # print(delta)
# # #     print(weekday,end=" ")

# y=input()
# x=input()
# print(x+y)hh
a =10
b=20
del a
c=a+b
print(c)