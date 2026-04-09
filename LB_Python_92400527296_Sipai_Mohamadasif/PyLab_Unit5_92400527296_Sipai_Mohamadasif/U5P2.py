'''Python program of Pie-chart with all parameters of a sample data. '''

import matplotlib.pyplot as plt

labels = ["Math", "Science", "English", "Computer", "History"]
sizes = [85, 90, 78, 92, 74]
colors = ["gold", "lightblue", "lightgreen", "pink", "orange"]
explode = (0, 0.1, 0, 0, 0)

plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Student Marks Distribution")
plt.legend(labels)
plt.axis("equal")
plt.show()