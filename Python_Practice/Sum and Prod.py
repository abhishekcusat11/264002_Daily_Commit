import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))


# Sample Input

# 2 2
# 1 2
# 3 4
# Sample Output

# 24
# Explanation

# The sum along axis  = [ ]
# The product of this sum = 24