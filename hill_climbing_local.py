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

def tweak(num, alpha):
    while function(num + alpha) < function(num):
        num += alpha 
    while function(num - alpha) < function(num):
        num -= alpha
    return num

def hill_climbing(initial, iteration1, iteration2, alpha):
    s = initial 
    best = s 
    for i in range(0,iteration1):
        r = tweak(s, alpha)
        for j in range(0, iteration2):
            w = tweak(s, alpha)
            if function(w) < function(r):
                r = w  
        s = r
        if function(s) < function(best):
            best = s
    return best 

def seeded_hill_climbing():
    result = []
    alpha = 0.0001
    iteration1 = 1000
    iteration2 = 10
    for i in range(1,31):
        np.random.seed(i)
        x = np.random.random()
        x = hill_climbing(x, iteration1, iteration2, alpha)
        result.append(x)
    return result

x_opt = seeded_hill_climbing()
y_opt = [function(num) for num in x_opt]
plt.scatter(x_opt, y_opt, c = 'r', marker = 'x')
graph_func('Finding the global minimum using Hill Climbing')
plt.show()
