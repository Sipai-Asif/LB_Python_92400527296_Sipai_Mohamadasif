'''Python program of Barplot with all parameters of a sample data'''

import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "Computer", "History"]
marks = [85, 90, 78, 92, 74]

plt.bar(
    subjects,
    marks,
    color="skyblue",
    edgecolor="black",
    width=0.6,
    label="Marks"
)

plt.title("Student Marks Bar Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()