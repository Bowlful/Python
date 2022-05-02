import numpy as np

x_data = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]).reshape(10,1)
t_data = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1]).reshape(10,1)

print("x_data.shape = ", x_data.shape, ", t_data.shape = ", t_data.shape)

W = np.random.rand(1,1)
b = np.random.rand(1)

print("w = ", W, ", w.shape = ", W.shape, ", b = ", b, ", b.shape = ", b.shape)

def derivative(f, x) :
    delta_x = 1e-4
    grad = np.zeros_like(x)

    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index

        tmp_val = x[idx]
        x[idx] = float(tmp_val) + delta_x
        fx1 = f(x)

        x[idx] = float(tmp_val) - delta_x
        fx2 = f(x)
        grad[idx] = (fx1 - fx2) / (2*delta_x)

        x[idx] = tmp_val
        it.iternext()
    return grad

def sigmoid(z):
    return 1 / (1+np.exp(-z))

def loss_func(x, t):
    delta = 1e-7

    z = np.dot(x, W) + b
    y = sigmoid(z)
    
    return -np.sum( t*np.log(y + delta) + (1-t)*np.log((1-y)+delta))

def loss_val(x, t):
    delta = 1e-7

    z = np.dot(x, W) + b
    y = sigmoid(z)
    
    return -np.sum( t*np.log(y + delta) + (1-t)*np.log((1-y)+delta))

def predict(test_data):

    z = np.dot(test_data, W) + b
    y = sigmoid(z)

    if y >= 0.5:
        result = 1
    else:
        result = 0
    
    return y , result
    
learning_rate = 1e-2

f = lambda x : loss_func(x_data, t_data)

print("Initial loss value = ", loss_val(x_data, t_data))

for step in range(50001):
    
    W -= learning_rate * derivative(f, W)
    
    b -= learning_rate * derivative(f, b)
    
    if (step % 5000 == 0):
        print("step = ", step, "loss value = ", loss_val(x_data, t_data))

test_data = np.array([3.5])

(real_val, logical_val) = predict(test_data)

print(real_val, logical_val)