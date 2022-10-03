# Sample code for generation of first example
import numpy as np

# from matplotlib import pyplot as plt
# pyplot imported for plotting graphs

x = np.linspace(0, 5, 6)

# numpy.linspace creates an array of
# 9 linearly placed elements between
# -4 and 4, both inclusive
y = np.linspace(0, 5, 6)

# The meshgrid function returns
# two 2-dimensional arrays
x_1, y_1 = np.meshgrid(x, y)

print("x_1 = ")
print(x_1)
print("y_1 = ")
print(y_1)

import matplotlib.pyplot as plt


# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x_1, y_1)
plt.show()