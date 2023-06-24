import matplotlib.pyplot as plt
import test1

fig, ax = plt.subplots()

ax.plot(test1.years, test1.irrs, alpha=0.5)

ax.scatter(test1.years, test1.irrs)

ax.axes.xaxis.set_ticks(range(0,49,2))

fig.autofmt_xdate()

plt.show()
