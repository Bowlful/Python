import numpy as np
from CH06_Example_Logic_Gate import *

x_data = np.array([[0,0], [0, 1], [1, 0], [1, 1]])
t_data = np.array([0,0,0,1])

AND_obj = LogicGate("AND_GATE", x_data, t_data)
AND_obj.train()

x_data = np.array([[0,0], [0, 1], [1, 0], [1, 1]])
t_data = np.array([0,1,1,1])

OR_obj = LogicGate("OR_GATE", x_data, t_data)
OR_obj.train()

x_data = np.array([[0,0], [0, 1], [1, 0], [1, 1]])
t_data = np.array([1,1,1,0])

NAND_obj = LogicGate("NAND_GATE", x_data, t_data)
NAND_obj.train()

input_data = np.array([[0,0], [0,1], [1,0], [1,1]])

s1 = []
s2 = []

new_input_data = []
final_output = []

for index in range(len(input_data)):
    s1 = NAND_obj.predict(input_data[index])
    s2 = OR_obj.predict(input_data[index])

    new_input_data.append(s1[-1])
    new_input_data.append(s2[-1])

    (sigmoid_val, logical_val) = AND_obj.predict(np.array(new_input_data))

    final_output.append(logical_val)
    new_input_data = []

for index in range(len(input_data)):
    print(input_data[index], " = ", final_output[index])