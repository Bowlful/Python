import numpy as np

loaded_data = np.loadtxt('./data-01-test_score.csv', delimiter=',', dtype=np.float32)

x_data = loaded_data[:,0:-1] 
t_data = loaded_data[:,[-1]]

print("x_data.ndim = ", x_data.ndim, "x_data.shape = ", x_data.shape)
print("t_data.ndim = ", t_data.ndim, "t_data.shape = ", t_data.shape)

W = np.random.rand(3,1)
b = np.random.rand(1)

print("W = ", W, ", W.shape = ", W.shape, ", b = ", b, ". b,shape = ", b.shape)

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

def loss_func(x, t):
    y = np.dot(x,W) + b
    
    return (np.sum((t-y)**2)) / (len(x))
    
def loss_val(x, t):
    y = np.dot(x,W) + b
    
    return (np.sum((t-y)**2)) / (len(x))

def predict(x):
    y = np.dot(x,W) + b
    
    return y

learning_rate = 1e-5

f = lambda x : loss_func(x_data, t_data)

print("Initial loss value = ", loss_val(x_data, t_data))

for step in range(30001):
    
    W -= learning_rate * derivative(f, W)
    
    b -= learning_rate * derivative(f, b)
    
    if (step % 3000 == 0):
        print("step = ", step, "loss value = ", loss_val(x_data, t_data))

test_data = np.array([100, 98, 81])

print(predict(test_data))