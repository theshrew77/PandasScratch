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
N = df.size
s = float(df.std())
Y = float(df.mean())
alpha = 0.05
MeanConfidenceInterval = Y + np.asarray(stats.t(df=N-1).ppf((alpha/2,1-alpha/2)))*s/np.sqrt(N)
#print(stats.t(df=5).ppf((0.025,0.975)))

print(MeanConfidenceInterval)