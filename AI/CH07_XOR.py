import numpy as np
from CH07_Logic_Gate import *

x_data = np.array([[0,0],[0,1],[1,0],[1,1]])
t_data = np.array([0,1,1,0])

xor_obj = LogicGate("XOR", x_data, t_data, 2)
xor_obj.train()

test_data = np.array([[0,0],[0,1],[1,0],[1,1]])

for data in test_data:
    (sigmoid_val, logical_val) = xor_obj.predict(data)
    print(data, "=", logical_val)