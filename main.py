"""
================ Phi Calculator in Python ================
"""


def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(0, n-2):
            temp = a + b
            a = b
            b = temp
        return b


def phi(iterations):
    return fibonacci(iterations) / fibonacci(iterations - 1)


try:
    iterations = input("Enter number of iterations: ")
    print("Phi approximation in", iterations, "iterations:", str(phi(int(iterations))))
    print("Phi approximation on Google: 1.6180339887")
    input("Press enter to exit application.")
except:
    input("An error occured. Press enter to exit application")
