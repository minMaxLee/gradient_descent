import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return ((6*x-2)**2)*np.sin(12*x-4)

def graph_func(title):
    x = np.linspace(0,1,100)
    y = function(x)
    plt.plot(x,y, c = 'b')
    plt.title(str(title))
    plt.xlabel('x values')
    plt.ylabel('y values')

def f_prime(x):
    return 12*((6*x-2)**2)*np.cos(4-12*x) - 12*(6*x-2)*np.sin(4-12*x)

def gradient_descent(initial, alpha):
    x = initial
    gradient = f_prime(x)
    while gradient > 0.001 or gradient < -0.001: 
        x -= (alpha*gradient)
        gradient = f_prime(x)
    return x 

def seeded_gradient_descent():
    result = [] 
    alpha = 0.001
    for i in range(1,31):
        np.random.seed(i)
        x = np.random.random()
        x = gradient_descent(x, alpha)
        result.append(x)
    return result 

x_opt = seeded_gradient_descent()
y_opt = [function(num) for num in x_opt]
plt.scatter(x_opt, y_opt, c ='r', marker = 'x')
graph_func('Finding local minimums using Gradient Descent')
plt.show()
