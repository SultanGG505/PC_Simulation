import matplotlib.pyplot as plt
import numpy as np


plt.plot([1,2,3,4])
plt.show()

def epsSys(arrX, arrY):
    sumX, sumY, sumX2, sumXY = 0, 0, 0, 0
    for i in range(0, len(arrX)):
        sumX += arrX[i]
        sumY += arrY[i]
        sumX2 += arrX[i] * arrX[i]
        sumXY += arrX[i] * arrY[i]
    print(sumX, sumY, sumX2, sumXY)
    arr1 = [sumX2, sumX]
    arr2 = [sumX, len(arrX)]
    arr3 = [sumXY, sumY]
    print(arr1, arr2, arr3)
    return arr1, arr2, arr3


# sumX2 * a + sumX * b = sumXY
# sumX * a + N * b = sumY

def cramer(arrs):
    mainDet = np.linalg.det(np.array([arrs[0], arrs[1]]))
    print(round(mainDet, 4))
    det1 = np.linalg.det(np.array([arrs[2], arrs[1]]))
    print(round(det1, 4))
    det2 = np.linalg.det(np.array([arrs[0], arrs[2]]))
    print(round(det2, 4))
    a = round((det1 / mainDet), 2)
    b = round((det2 / mainDet), 2)
    print(a)
    print(b)


cramer(epsSys([1, 2, 3, 4, 5, 6], [1.0, 1.5, 3.0, 4.5, 7.0, 8.5]))
