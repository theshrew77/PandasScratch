import csv
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy import stats
import numpy as np
import statistics as st
import math
from mpl_toolkits import mplot3d
from matplotlib import rc
from pylab import MaxNLocator
import pandas as pd
import datetime as dt
import NISTplots as nist

Variable = 'Deflection'
#open the data file
df = pd.read_csv('LEW.DAT', names=[Variable],skiprows=range(0,25),header=None,delim_whitespace=True)


#create the four plot for the data
nist.FourPlot(df,Variable,(-2500,2500,100))

fig = plt.figure()
axes = fig.add_subplot()
pd.plotting.autocorrelation_plot(df[Variable], ax=axes)
plt.show()

Nsamples = df.size
t = np.linspace(0,(Nsamples-1)/Nsamples,Nsamples)

hanning = 0.5-0.5*np.cos(2*math.pi*t)
ybar = df[Variable].mean()
df[Variable + ' Fluctuation'] = df[Variable] - df[Variable].mean()
df[Variable + ' Windowed'] = df[Variable + ' Fluctuation']*hanning

y = fft(df[Variable + ' Windowed'].values)
Y = abs(y)/(Nsamples/2)
Y[0] /= 2

plt.plot(t[:int(Nsamples/2-1)],Y[:int(Nsamples/2-1)])
plt.show()

print(df[Variable].describe())

P = np.polyfit(df.index,df[Variable],1)
print(P)
