#initially i got error,since i saved file name as matplotlib.py


#Importing pyplot
from matplotlib import pyplot as plt
#we can import style
from matplotlib import style 
plt.style.use('ggplot')

#Plotting to our canvas
plt.plot([1,2,3],[4,5,1])
#mark and join the points in graph 
plt.title('Testing matplotlib')
plt.xlabel('x axis')
plt.ylabel('y axis')
#Showing what we plotted
plt.show()
