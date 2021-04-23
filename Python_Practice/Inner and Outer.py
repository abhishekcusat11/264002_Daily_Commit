import numpy
A=numpy.array(input().split(),int)
B=numpy.array(input().split(),int)
print(numpy.inner(A,B))
print(numpy.outer(A,B))

# Sample Input

# 0 1
# 2 3
# Sample Output

# 3
# [[0 0]
#  [2 3]]
