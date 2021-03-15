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

cols = ['CRYSTID', 'CHECKID', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'OPER', 'HUMIDITY', 'PROBEID', 'TEMP', 'CHECKSTD', 'STDDEV', 'DF']
df = pd.read_csv('MPC62.DAT', names=cols,skiprows=range(0,50),header=None,delim_whitespace=True)

print('len(df) = ', len(df))




s_1 = np.sqrt(np.mean(df['STDDEV']**2))
s_2 = df['CHECKSTD'].std()
print('Level 1 standard deviation = ',np.round(s_1,5),' ohm.cm')
print('Level 2 standard deviation = ',np.round(s_2,5),' ohm.cm')

fig = plt.figure()
ax = plt.subplot(2,1,1)
df['CHECKSTD'].plot.hist(bins=8)


ax = plt.subplot(2,2,1)
stats.probplot(df['CHECKSTD'],plot=ax)

plt.show()