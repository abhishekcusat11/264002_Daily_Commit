import numpy
n= int(raw_input())
a = [map(int,raw_input().split()) for _ in range(n)]
b = [map(int,raw_input().split()) for _ in range(n)]
print numpy.dot(a,b)


# Sample Input

# 2
# 1 2
# 3 4
# 1 2
# 3 4
# Sample Output

# [[ 7 10]
#  [15 22]]