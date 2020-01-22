import matplotlib.pyplot as plt

x_val = list(range(1, 5001))
y_val = [x**3 for x in x_val]

plt.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Reds)

plt.show()
