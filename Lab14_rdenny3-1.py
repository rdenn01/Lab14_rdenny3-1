"""
Cosine Function Plot
Ryan Denny

The purpose of this program is to use matplotlib to plot the cosine function.

8/9/2025
"""

import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()

x_numbers = [x / 10.0 for x in range (1, 500, 1)]
y_numbers = [math.cos(x) for x in x_numbers]

ax.set_title('Cosine Function')

ax.tick_params(labelsize=10)

plt.plot(x_numbers, y_numbers, color='red', linewidth=3)
plt.show()