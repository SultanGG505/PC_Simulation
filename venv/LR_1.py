import matplotlib.pyplot as plt
import numpy as np
# plt.plot([1,2,3,4])
# plt.show()

def epsSys(arrX, arrY):
    sumX, sumY, sumX2, sumXY = 0, 0, 0, 0
    for i in range(0, len(arrX)):
        sumX += arrX[i]
        sumY += arrY[i]
        sumX2 += arrX[i] * arrX[i]
        sumXY += arrX[i] * arrY[i]
    print(sumX, sumY, sumX2, sumXY)
    return sumX, sumY, sumX2, sumXY

# sumX2 * a + sumX * b = sumXY
# sumX * a + N * b = sumY

def detsAndA_B():
    mainDet =


epsSys([1, 2, 3, 4, 5, 6], [1.0, 1.5, 3.0, 4.5, 7.0, 8.5])
