import numpy as np

def sigmoid(x) :
    return 1 / (1+np.exp(-x))

def derivative(f, var):
    delta_x = 1e-4
    grad = np.zeros_like(var)

    it = np.nditer(var, flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index

        tmp_val = var[idx]
        var[idx] = float(tmp_val) + delta_x
        fx1 = f(var)

        var[idx] = float(tmp_val) - delta_x
        fx2 = f(var)
        grad[idx] = (fx1 - fx2) / (2*delta_x)

        var[idx] = tmp_val
        it.iternext()
    return grad

class LogicGate:
    def __init__(self, gate_name, x_data, t_data):
        self.name = gate_name
        self.x_data = x_data.reshape(4,2)
        self.t_data = t_data.reshape(4,1)
        self.W = np.random.rand(2,1)
        self.b = np.random.rand(1)
        self.lerning_rate = 1e-2

    def loss_func(self):

        delta = 1e-7

        z = np.dot(self.x_data, self.W) + self.b
        y = sigmoid(z)

        return -np.sum(self.t_data*np.log(y+delta)+(1-self.t_data)*np.log((1-y)+delta))

    def loss_val(self):

        delta = 1e-7
        
        z = np.dot(self.x_data, self.W) + self.b
        y = sigmoid(z)

        return -np.sum(self.t_data*np.log(y+delta)+(1-self.t_data)*np.log((1-y)+delta))

    def train(self):

        f = lambda x : self.loss_func()
        print("Initial loss value = ", self.loss_val())

        for step in range(20001):
            
            self.W -= self.lerning_rate * derivative(f, self.W)
            self.b -= self.lerning_rate * derivative(f, self.b)

            if (step % 1000 == 0):
                print("step = ", step, "loss value = ", self.loss_val())

    def predict(self, input_data):
        z = np.dot(input_data, self.W) + self.b
        y = sigmoid(z)

        if y > 0.5:
            result = 1
        else:
            result = 0
        
        return y, result