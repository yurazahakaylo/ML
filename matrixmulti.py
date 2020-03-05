import random 
import time
import numpy as np

col = 100
row = 100
matrix1 = [[random.randrange(0, 10) for a in range(col)] for b in range(row)]
matrix2 = [[random.randrange(0, 10) for a in range(col)] for b in range(row)]
matrix3 = [[0 for a in range(col)] for b in range(row)]
start_time = time.time()

for i in range(0, row):
    for j in range(0, col):
        for k in range(0, col):
            matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
print("usual time")
print("--- %s seconds ---" % (time.time() - start_time))
matrix3 = [[0 for a in range(col)] for b in range(row)]
start_time = time.time()
matrix3 = np.dot(matrix1, matrix2)
print("time with numpy")
print("--- %s seconds ---" % (time.time() - start_time))

