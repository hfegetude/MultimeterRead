import matplotlib.pyplot as plt
import pylab

def SavePlotData(x_vector, y_vector):
	plt.plot(x_vector, y_vector)
	plt.ylabel('Voltage')
	plt.xlabel('Time')
	pylab.savefig('plot.png')
