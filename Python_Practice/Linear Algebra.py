import numpy
print(round(numpy.linalg.det(numpy.array([list(map(float,input().split())) for _ in range(int(input()))])),2))


# Sample Input

# 2
# 1.1 1.1
# 1.1 1.1
# Sample Output

# 0.0