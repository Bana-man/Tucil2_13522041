from inspect import getgeneratorlocals
from typing import List
from Util import *
import time
import numpy as np
import matplotlib.pyplot as plt

def BaseBezier(pointSet: List[Point]) -> List[Point]:
    global timeDnC
    lenSet = len(pointSet)
    pointList = pointSet

    counterIdx = 1
    resultList = [pointSet[0], pointSet[lenSet-1]]

    while (lenSet > 2):
        pointListTemp = []

        time_start = 1000*time.perf_counter()
        for i in range(1, lenSet):
            pointListTemp.append(GetMiddlePoint(pointList[i-1], pointList[i]))

        pointList = pointListTemp
        lenSet -= 1
        resultList.insert(counterIdx, pointList[lenSet-1])
        resultList.insert(counterIdx, pointList[0])
        counterIdx += 1
        time_stop = 1000*time.perf_counter()
        a = time_stop - time_start
        timeDnC += a
        
        x = np.array([i.x for i in pointListTemp])
        y = np.array([i.y for i in pointListTemp])
        ax1.plot(x,y, color = 'black', linewidth = 1, ls = 'dashed')

    resultList.insert(counterIdx, GetMiddlePoint(pointList[0], pointList[1]))
       
    return resultList

def BezierPointGenerator(pointSet: List[Point], iteration: int, nControl: int):
    global color_list
    global iterationNow

    if (color_list[iterationNow-1][0] == 0):
        label = "Iteration " + str(iterationNow)
        color_list[iterationNow-1][0] = 1
        iterationNow += 1
    else:
        label = ""

    listPoint = [pointSet[i] for i in range(0, len(pointSet), nControl-1)]
    x = np.array([i.x for i in listPoint])
    y = np.array([i.y for i in listPoint])

    hex_color = '#{:02x}{:02x}{:02x}'.format(*color_list[iteration-1][1])
    ax1.plot(x,y, color = hex_color, linewidth = 1, label = label)

    if (iteration != 0):
        setBaru = BaseBezier(pointSet)

        BezierPointGenerator(setBaru[:nControl], iteration-1, nControl)
        BezierPointGenerator(setBaru[nControl-1:], iteration-1, nControl)

def DivideNConquer(controlSet: List[Point], iteration: int):
    BezierPointGenerator(controlSet, iteration, len(controlSet))

def findPointBruteforce(controlSet: List[Point], xValue: int):
    resultX = 0
    resultY = 0
    lenSet = len(controlSet)
    for i in range(lenSet):
        a = ((1 - xValue)**(lenSet - 1 - i))*(xValue**i)*getCombination(lenSet-1, i)
        resultX += a*controlSet[i].x
        resultY += a*controlSet[i].y
    return resultX, resultY

def BruteForce(controlSet: List[Point], iteration: int):
    global timeBF
    xResult = []
    yResult = []

    
    time_start = time.perf_counter()

    i = 0
    while i <= 1:
        x, y = findPointBruteforce(controlSet, i)
        
        xResult.append(x)
        yResult.append(y)
        i += (1/(2**iteration))

    time_stop = time.perf_counter()
    a = 1000*time_stop - 1000*time_start
    timeBF += a

    ax2.plot(np.array(xResult), np.array(yResult), color = 'r')

a = [Point(0,0), Point(1,5), Point(5,4), Point(6,0), Point(4,-2)]

fig2, ax2 = plt.subplots()
ax2.set_title('Bruteforce')
timeBF = 0
fig1, ax1 = plt.subplots()
ax1.set_title('Divide and Conquer')
timeDnC = 0

BruteForce(a, 3)
DivideNConquer(a, 3)

print("Execution Time:")
print(round(timeBF,3), 'ms Bruteforce')
print(round(timeDnC,3), 'ms DnC')

plt.legend()
plt.show()
