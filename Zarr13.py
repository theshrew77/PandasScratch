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

Variable = 'Calibration Factor'
#open the data file
df = pd.read_csv('ZARR13.DAT', names=[Variable],skiprows=range(0,25),header=None,delim_whitespace=True)

print(df[Variable].describe())
print('Median = ', df[Variable].median(),'\r\n')

#create the four plot for the data
nist.FourPlot(df,Variable)

#calculate mean confidence interval
N = df.size
s = float(df.std())
Y = float(df.mean())
alpha = 0.05
MeanConfidenceInterval = Y + np.asarray(stats.t(df=N-1).ppf((alpha/2,1-alpha/2)))*s/np.sqrt(N)
print('Mean confidence interval =', MeanConfidenceInterval, '\n')

#test hypothesis that population mean = u0
u0 = 9.26
T = (Y-u0)*np.sqrt(N)/s
CriticalValue = max(np.asarray(stats.t(df=N-1).ppf((alpha/2,1-alpha/2))))
if abs(T) > CriticalValue:
    print("|%4.2f| > %.2f, null hypothesis pop. mean = %.2f rejected\n" %(T,CriticalValue,u0))
if abs(T) <= CriticalValue:
    print("|%4.2f| <= %.2f, null hypothesis pop. mean = %.2f accepted\n" %(T,CriticalValue,u0))


