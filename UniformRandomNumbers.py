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



#open the data file
Variable = 'Random Numbers'
df = pd.read_csv('RANDU.DAT', skiprows=range(0,25),header=None,delim_whitespace=True)
#convert the matrix of random numbers into 1 long list
ds=pd.Series(df.values.ravel('F'))
df = pd.DataFrame(ds,columns = [Variable])
print(df[Variable].describe())
print('Median = ', df[Variable].median(),'\r\n')

#create the four plot for the data
nist.FourPlot(df,Variable,(-2,3,50),'uniform')

#fig = plt.figure()
#axes = fig.add_subplot()
distributions = ['norm','uniform']
distributions = ['norm','uniform']
for Dist in distributions:
    (osm, osr),(slope, intercept, r) = stats.probplot(df[Variable].values,dist = Dist)
    print(Dist, ' correlation = ', r,'\r')

P = np.polyfit(df.index,df[Variable],1)
print("Run Plot linear fit parameters = ",P)



#pd.plotting.bootstrap_plot(df[Variable], fig=fig,samples=100)
#plt.xlim([0.4,0.6])
#plt.show()

Samples = 1000
Size = 100

SampleStats = pd.DataFrame(columns = ['means','medians','midranges'])
Entry = {"means":0, "medians":0, "midrange":0}
for i in range(Samples):
    sample = df[Variable].sample(Size,replace = True)
    Entry['means'] = sample.mean()
    Entry['medians'] = sample.median()
    Entry['midranges'] = (sample.max() + sample.min())/2
    SampleStats = SampleStats.append(Entry, ignore_index = True)
 

fig, axes = plt.subplots(2,3)

Bins = np.linspace(0.4,0.6,25)
Confidence = 0.95
axes[0,0].plot(SampleStats['means'].values)
axes[0,1].plot(SampleStats['medians'].values)
axes[0,2].plot(SampleStats['midranges'].values)
SampleStats['means'].hist(ax=axes[1,0],color='k',bins=Bins)
SampleStats['medians'].hist(ax=axes[1,1],color='k',bins=Bins)
SampleStats['midranges'].hist(ax=axes[1,2],color='k',bins=Bins)
plt.show()

SortedMeans = SampleStats['means'].sort_values()
SortedMidrange = SampleStats['midranges'].sort_values()
MeanMean = SampleStats['means'].mean()
MidrangeMean = SampleStats['midranges'].mean()
i = int(round((1-Confidence)/2*Samples,0))
j = int((1+Confidence)/2*Samples)
print('Mean:', 
    round(MeanMean,4),
    Confidence*100, 
    'confidence interval = (', 
    round(SortedMeans.iloc[i],4),
    ', ',
    round(SortedMeans.iloc[j],4),
    ')',
    'width = ', 
    round(SortedMeans.iloc[j]-SortedMeans.iloc[i],4),
    '\r'
    )
print('Midrange:',
    round(MidrangeMean,4),
    Confidence*100, 
    'confidence interval = (', 
    round(SortedMidrange.iloc[i],4), 
    ', ',
    round(SortedMidrange.iloc[j],4),
    ')'
    , 'width = ', 
    round(SortedMidrange.iloc[j]-SortedMidrange.iloc[i],4),
    '\r'
    )

