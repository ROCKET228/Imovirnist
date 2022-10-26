import math
import matplotlib.pyplot as plt

def setData(fileName, data):
    file = open(fileName, 'r')
    for line in file:
        data.append(int(line.strip()))


data = []
setData('input_100_lab_1.txt', data)


#1

def TableForTask1(data):
    print("Xi\t fi\t\t\t\t Rf\t\t\t\tFi\t")
    count = 1
    N = 0
    for i in data:
        N += i
    sum2 = 0
    for i in data:
        sum2 += i
        print(count, "\t", i, "\t\t\t", round(i/N, 3), "\t\t\t", sum2)
        count += 1
    print("Total:", N)

TableForTask1(data)

MostView = 0

for i in range(len(data)):
    if data[i] > MostView:
        MostView = data[i]

print("Most views:", MostView)



#2
sum = 0

for i in range(len(data)):
    sum += data[i]

Mediana = sum/len(data)

print("Mediana:", Mediana)

Moda = 0
ModaAnswer = 0
counter = 0

for i in range(len(data)):
    Moda = data[i]
    temp = 0
    for j in range(len(data)):
        if Moda == data[j]:
            temp +=1
            if temp > counter:
               counter = temp
               ModaAnswer = data[i]

print("Moda: ", ModaAnswer)

#3
SquareDeviation = 0

for i in data:
     SquareDeviation += (i-Mediana)**2

Variance = (SquareDeviation/len(data))

print("Variance:", Variance)

MeanSquareDeviation = math.sqrt(Variance)

print("Mean Square Deviation:", MeanSquareDeviation)

#4
plt.bar(range(len(data)), data)

plt.xlabel("Film")
plt.ylabel("Frequency of views")
plt.show()