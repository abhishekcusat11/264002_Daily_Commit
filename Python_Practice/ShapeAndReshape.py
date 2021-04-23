import numpy
change_array = numpy.array([list(map(int, input().split()))])
print(numpy.reshape(change_array, (3,3)))

# Sample Input

# 1 2 3 4 5 6 7 8 9
# Sample Output

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]