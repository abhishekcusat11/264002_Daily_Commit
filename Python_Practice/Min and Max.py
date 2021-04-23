import numpy as np

n, m = list(map(int, (input().split())))
a = np.array([list(map(int,(input().split()))) for i in range(int(n))])
print(np.max(np.min(a, axis = 1), axis = None))




# Sample Input

# 4 2
# 2 5
# 3 7
# 1 3
# 4 0
# Sample Output

# 3
# Explanation

# The min along axis 1  = [2,3,1,0]
# The max of [2,3,1,0]  = 3