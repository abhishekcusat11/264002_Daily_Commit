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
for i in range(10):
    try: 
        if 10 / i == 2.0:
            break
        except ZeroDivisionError:
            print(1)
        else:
            print(2)