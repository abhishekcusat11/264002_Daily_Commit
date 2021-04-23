import numpy
d = tuple(  map(int,(input().split())     ))

arr1 = numpy.zeros((d), dtype = numpy.int)
print(arr1)
    
arr2 = numpy.ones((d), dtype = numpy.int)
print(arr2)


# Sample Input 0

# 3 3 3
# Sample Output 0

# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]
# [[[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]]