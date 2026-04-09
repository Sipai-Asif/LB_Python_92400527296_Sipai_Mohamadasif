'''Python program of Box Plot with all parameters of a sample data. '''

import matplotlib.pyplot as plt

data = [12, 15, 14, 10, 18, 20, 17, 13, 16, 19]

plt.boxplot(
    data,
    notch=True,
    vert=True,
    patch_artist=True,
    widths=0.5,
    showmeans=True,
    meanline=True,
    showfliers=True,
    labels=["Marks"]
)

plt.title("Box Plot of Sample Data")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.grid(True)

plt.show()