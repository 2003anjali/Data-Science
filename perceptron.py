import numpy as np

def step_func(x):
    if x>=0 :
        return 1
    else :
        return 0
def perceptron(weights, bias, x):
    calculation=np.dot(weights,x)+bias
    return step_func(calculation)
weights=[2,2]
bias=-3
output=perceptron(weights,bias,[0,0])
print(output)
output=perceptron(weights,bias,[0,1])
print(output)
output=perceptron(weights,bias,[1,0])
print(output)
output=perceptron(weights,bias,[1,1])
print(output)

import numpy as np

def step_func(x):
    if x>=0 :
        return 1
    else :
        return 0
def perceptron(weights, bias, x):
    calculation=np.dot(weights,x)+bias
    return step_func(calculation)
weights=[1,1]
bias=-0.5
output=perceptron(weights,bias,[0,0])
print(output)
output=perceptron(weights,bias,[0,1])
print(output)
output=perceptron(weights,bias,[1,0])
print(output)
output=perceptron(weights,bias,[1,1])
print(output)