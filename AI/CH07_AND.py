import numpy as np
from CH07_Logic_Gate import *

x_data = np.array([[0,0],[0,1],[1,0],[1,1]])
t_data = np.array([0,0,0,1])

xor_obj = LogicGate("AND", x_data, t_data, 1)
xor_obj.train()

test_data = np.array([[0,0],[0,1],[1,0],[1,1]])

for data in test_data:
    (sigmoid_val, logical_val) = xor_obj.predict(data)
    print(data, "=", logical_val)