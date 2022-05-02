import numpy as np
from CH06_Example_Logic_Gate import *

x_data = np.array([[0,0], [0, 1], [1, 0], [1, 1]])
t_data = np.array([0,0,0,1])

AND_obj = LogicGate("AND_GATE", x_data, t_data)
AND_obj.train()

test_data = np.array([[0,0], [0,1], [1,0], [1,1]])
for input_data in test_data:
    (sigmoid_val, logical_val) = AND_obj.predict(input_data)
    print(input_data, " = ", logical_val)