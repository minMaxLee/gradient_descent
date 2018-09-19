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

def global_gradient_descent(initial, iteration, alpha):
    x = initial 
    result = x
    for i in range(0, iteration):
        gradient = f_prime(x)
        while gradient > 0.001 or gradient < -0.001:
            x -= (alpha * gradient)
            gradient = f_prime(x)
        if function(x) < function(result):
            result = x
        x = np.random.random()
    return result 
  
def seeded_global_gradient_descent():
    result = []
    alpha = 0.0001
    iteration = 100 
    for i in range(1,31):
        np.random.seed(i)
        x = np.random.random()
        x = global_gradient_descent(x, iteration, alpha)
        result.append(x)
    return result 

x_opt = seeded_global_gradient_descent()
y_opt = [function(num) for num in x_opt]
plt.scatter(x_opt, y_opt, c = 'r', marker = 'x')
graph_func('Finding global minimum using Gradient Descent')
plt.show()
