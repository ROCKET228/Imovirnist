import numpy as np

def P(b, total):
    return (b / total)

def A(n, m):
    b = (np.math.factorial(n)/np.math.factorial(n - m))
    return b

def fact(n, m):
    b = (np.math.factorial(n) * np.math.factorial(m-3))/(np.math.factorial(m)*np.math.factorial(n-3))
    return b

def dob_fact(a, p, m, n):
    b = (p / n) * fact(a, m)
    return b

def task1(b, br, r, bl):
    print()
    print("Task 1:")
    total = b + br + r + bl
    print("A box taken at random will be black =", P(b, total))
    print("A box taken at random will be brown =", P(br, total))
    print("A box taken at random will be red =", P(r, total))
    print("A box taken at random will be blue =", P(bl, total)),
    print("A box taken at random will be red or blue =", P(bl, total) + P(r, total))

def task2(n, n1, m):
    print()
    print("Task 2:")
    A1 = A(n, m)
    A2 = A(n1, m)
    print("The probability that among two randomly selected employees, at least one will be a consultant =", (A1 - A2) / A1)

def task3(n, n1, m):
    print()
    print("Task 3:")
    A1 = A(n, m)
    A2 = A(n1, m)
    print("The probability that there will be at least one of the relatives among the selected specialists =", (A1 - A2) / A1)

def task4(p1, p2, p3, p4):
    print()
    print("Task 4:")
    print("The probability that this item is destined for the fifth department =", (1 - (p1 + p2 + p3 + p4)))

def task5(p1, a1):
    print()
    print("Task 5:")
    print("The probability of the arrival of two shunting trains on two adjacent tracks =", ((p1/a1) * ((p1-1)/(a1-1))))

def task6(p1, p2):
    print()
    print("Task 6:")
    print("The probability that the product of the first grade is produced by this machine =", (p1 * p2))

def task7(p1, p2, p3, p4, a1, a2, a3, a4, m, n):
    print()
    print("Task 7:")
    b = dob_fact(a1, p1, m, n) + dob_fact(a2, p2, m, n) + dob_fact(a3, p3, m, n) + dob_fact(a4, p4, m, n)
    print("The probability that this student is prepared: \nа) perfectly = ", dob_fact(a1, p1, m, n) / b)
    print("б) badly = ", dob_fact(a4, p4, m, n) / b)

def task8(p1, p2, p3, a1, a2, a3):
    print()
    print("Task 8:")
    print("The probability that a piece taken at random is standard =", ((p1*a1) + (p2*a2) + (p3*a3)))

def task9(p1, p2, p3, a1, a2, a3):
    print()
    print("Task 9:")
    print("The probability that the patient had peritonitis =", ((p2 * a2)/((p1 * a1) + (p2 * a2) + (p3 * a3))))

def task10(p1, p2, a1, a2):
    print()
    print("Task 10:")
    print("The probability that the device is assembled by a highly qualified specialist =", ((p1 * a1) / ((p1 * a1) + (p2 * a2))))

task1(40, 26, 22, 12)
task2(10, 2, 2)
task3(10, 8, 3)
task4(0.15, 0.25, 0.2, 0.1)
task5(80, 120)
task6(0.9, 0.8)
task7(3, 4, 2, 1, 20, 16, 10, 5, 20, 10)
task8(0.4, 0.3, 0.3, 0.9, 0.95, 0.95)
task9(0.4, 0.3, 0.3, 0.8, 0.7, 0.85)
task10(0.3, 0.7, 0.9, 0.8)