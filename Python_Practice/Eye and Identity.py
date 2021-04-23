import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))


# Sample Input

# 3 3
# Sample Output

# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]