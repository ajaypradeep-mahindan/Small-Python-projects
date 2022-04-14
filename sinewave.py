#packages required for calling math and plotting graph
import numpy as np
import matplotlib.pyplot as plt
#setting value for range of grph 
time=np.arange(0,10,0.1)
#sin function
amp1=np.sin(time)
#cosine function
amp2=np.cos(time)
#plotting the graph
plt.plot(time,amp1)
plt.plot(time,amp2)
plt.title('Sine Wave(Blue) and Cosine Wave(Yellow)')#Title of pLOT
plt.xlabel('Time -->')#X AXIS
plt.ylabel('Amplitude -->')#y AXIS
plt.grid(True,which='Both')
plt.axhline(y=0,color='k')
plt.show()
