import matplotlib.pyplot as plt

nums = [x for x in range(1, 6)]
squares = [x**2 for x in nums]

plt.plot(nums, squares, linewidth=5)

# Set the chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()
