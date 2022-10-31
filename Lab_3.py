import math
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np



def connectstring(nameoffile):
    inputdata = []
    input = open(nameoffile)
    input.seek(1)
    for line in input:
        inputdata.append(input.read(3))
        input.read(1)
        inputdata.append(input.read(2))
    for i in range(int(len(inputdata))):
        inputdata[i] = inputdata[i].replace(',', '.')
    data = [[0 for i in range(2)] for j in range(int(len(inputdata) / 2))]
    index0 = 0
    index1 = 0
    for i in range(int(len(inputdata))):
        if i % 2 == 0:
            data[index0][0] = float(inputdata[i])
            index0 += 1
        elif i % 2 != 0:
            data[index1][1] = int(inputdata[i])
            index1 += 1
    return data

filename = input('Name of file:')
data = connectstring(filename)
data = sorted(data)

#1
def dataX(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][0])
    return inputdatadata

def dataY(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][1])
    return inputdatadata

def trend(data):
    if max(data)==data[len(data)-1]:
        print("Тренд позитивний")
    elif min(data)==data[len(data)-1]:
        print("Тренд негативний")
    else:
        print("Дані не мають терду")


#2
def Task2(x, y):
    global averagex, averagey
    covarience = 0.0
    for i in range(len(x)):
        averagex += x[i]
        averagey += y[i]
    averagex = averagex / len(x)
    averagey = averagey / len(y)
    for i in range(len(x)):
        covarience += (x[i] - averagex) * (y[i] - averagey)
    covarience = covarience / (len(x)-1)
    print('Covarince: ', covarience)

def Task4(x, y):
    global averagex, averagey
    correlation, sum1, sum2, sum3 = 0.0, 0.0, 0.0, 0.0
    for i in range(len(X)):
        sum1 = (x[i] - averagex) * (y[i] - averagey)
        sum2 = (x[i] - averagex) * (x[i] - averagex)
        sum3 = (y[i] - averagey) * (y[i] - averagey)
    sum2 += sum2 * sum3
    correlation = sum1/math.sqrt(sum2)
    print("Correlation: ", correlation)

#3
def Task3(x, y ):
    global averagex, averagey
    byx, sumxy, sumx, sumy, sumx2, sumy2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

    for i in range(len(x)):
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i] * y[i]
        sumx2 += x[i] * x[i]
        sumy2 += y[i] * y[i]
    byx = (len(x) * sumxy - (sumx * sumy)) / (len(x) * sumx2 - sumx2)
    x, y = sp.symbols("x, y")
    line = sp.Eq(y-averagey, byx * (x - averagex))
    linex = sp.solve(line, y)
    liney = sp.solve(line, x)

    print("x = ", liney)
    print("y = ", linex)





#input_100_lab_3.txt
X = dataX(data)
Y = dataY(data)
averagex, averagey = np.mean(X), np.mean(Y)
plt.scatter(X, Y)
trend(data)
plt.show()
Task2(X, Y)
Task3(X, Y)
Task4(X, Y)
