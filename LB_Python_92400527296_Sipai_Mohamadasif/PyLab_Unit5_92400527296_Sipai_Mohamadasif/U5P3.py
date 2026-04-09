'''Python program of Line plot with all parameters of a sample data.  '''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(
    x,
    y,
    color="blue",
    linestyle="--",
    linewidth=2,
    marker="o",
    markersize=8,
    markerfacecolor="red",
    markeredgecolor="black",
    label="Sales"
)

plt.title("Sales Line Plot")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.xlim(1, 5)
plt.ylim(0, 35)

plt.show()