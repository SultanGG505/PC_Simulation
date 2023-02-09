import matplotlib.pyplot as plt
import numpy as np

def plot(data, MSQ_arr):
    plt.plot(data[0], data[1], label="эксп.")
    plt.plot(data[0], MSQ_arr, label="МНК")
    plt.grid()
    plt.legend()
    plt.show()


data = []
with open("input.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
print(data)


def MSQ(arrX, arrY):
    sumX, sumY, sumX2, sumXY, n = 0, 0, 0, 0, len(arrX)
    for i in range(0, len(arrX)):
        sumX += arrX[i]
        sumY += arrY[i]
        sumX2 += arrX[i] * arrX[i]
        sumXY += arrX[i] * arrY[i]
    print(sumX, sumY, sumX2, sumXY)
    arr1 = [sumX2, sumX]
    arr2 = [sumX, n]
    arr3 = [sumXY, sumY]
    print(arr1, arr2, arr3)

    mainDet = np.linalg.det(np.array([arr1, arr2]))
    print(round(mainDet, 4))
    det1 = np.linalg.det(np.array([arr3, arr2]))
    print(round(det1, 4))
    det2 = np.linalg.det(np.array([arr1, arr3]))
    print(round(det2, 4))
    a = round((det1 / mainDet), 2)
    b = round((det2 / mainDet), 2)
    print(a)
    print(b)
    MSQ_Array_Y = []
    for i in range(0, n):
        newY = a * arrX[i] + b
        MSQ_Array_Y.append(newY)

    print(MSQ_Array_Y)
    return MSQ_Array_Y

MSQ_arr =  MSQ(data[0],data[1])
plot(data, MSQ_arr)