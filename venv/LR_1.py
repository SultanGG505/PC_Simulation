import matplotlib.pyplot as plt
import numpy as np


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
    return a, b


def plot(ab, data):
    plt.plot(data[0],data[1], label = "aboba")
    plt.legend()
    plt.show()

data = []
with open("input.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
print(data)

plot(cramer(epsSys(data[0], data[1])),data)

# print(len(data[0]))
