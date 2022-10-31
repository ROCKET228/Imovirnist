import math
import matplotlib.pyplot as plt

def setData(fileName, data):
    file = open(fileName, 'r')
    for line in file:
        data.append(int(line.strip()))


data = []
setData('input_100_lab_2.txt', data)


#1
print("Task 1")

Qr1 = (1/4)*(len(data)+1)
Qr2 = (3/4)*(len(data)+1)



Q1 = data[int(Qr1)-1] + (Qr1 - int(Qr1)) * (data[int(Qr1)] - data[int(Qr1)-1])
Q2 = data[int(Qr2)-1] + (Qr2 - int(Qr2)) * (data[int(Qr2)] - data[int(Qr2)-1])

print("Q1 = ",Q1)
print("Q2 = ",Q2)

P90 = (90/100)*(len(data) + 1)

print("P90 = ",P90)

#2
print(" ")
print("Task 2")

def mean(data):
  n = len(data)
  mean = sum(data) / n
  return mean


def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance


def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

print("Standard Deviation: ",stdev(data))
print("Mean Deviation: ", mean(data))


#3
print(" ")
print("Task 3")



a = (25/129)
b = (10400/129)


for i in range(len(data)):
    y = a * data[i] + b
    print(data[i], int(y))
    data[i] = y


#4

stems = [i for i in range(100)]
plt.xlim(0, 100)
plt.stem(stems, data)
plt.show()

#5
plt.boxplot(data)
plt.show()

