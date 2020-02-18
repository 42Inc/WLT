import matplotlib.pyplot as plt
import numpy as np

def radiocoverage(arg):
	x = np.arange(0, 2*(np.pi), 0.1)
	# setting the corresponding y - coordinates
	y = np.sin(x)
	# potting the points
	drawgraph(x, y)

def drawgraph(x, y):
	# potting the points
	plt.plot(x, y)
	# function to show the plot
	plt.show()

radiocoverage()
