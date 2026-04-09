'''Python program of Scatter Plot with all parameters of a sample 
data. '''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [10, 15, 13, 17, 20, 22]
sizes = [50, 100, 150, 200, 250, 300]
colors = ["red", "blue", "green", "purple", "orange", "brown"]

plt.scatter(
    x,
    y,
    s=sizes,
    c=colors,
    marker="o",
    alpha=0.8,
    edgecolors="black",
    label="Data Points"
)

plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.legend()
plt.xlim(0, 7)
plt.ylim(0, 25)

plt.show()