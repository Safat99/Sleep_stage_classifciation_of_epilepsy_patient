# -*- coding: utf-8 -*-
"""
Created on Fri Aug 6 18:11:48 2021

@author: Shamim
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##########################           PART ONE            ##########################
import os
os.chdir('annotations/') 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-v', '--version', required=True, help='version means nfle(10).. so 10 it is')
args = vars(ap.parse_args())

ver = args['version']
nfle = pd.read_csv("nfle"+str(ver)+".csv")
dataSize = nfle.shape[0]
nfle.head()
#dataSize = 5
df = nfle.loc[nfle["Location"]=="ROC-LOC"].loc[:,['Sleep Stage','Time [hh:mm:ss]','Event','Duration[s]']]
df = df.reset_index(drop=True)
dataSize = df.shape[0]



problemdf = df.loc[df["Duration[s]"]!=30]


df["timestamp"]=0
# df["DurationCalc"]=0

#nfle.columns
#h,m,s = map(int, df['Time [hh:mm:ss]'][0].split(':'))
#df["timestamp"][0] = h*3600+m*60+s
#df["DurationCalc"][0]=30
dur=30
for i in range(dataSize):
	h,m,s = map(int, df['Time [hh:mm:ss]'][i].split(':'))
	if h<20:
		h+=24
	df.loc[i,"timestamp"] = h*3600+m*60+s
	# df["DurationCalc"][i] = dur
	if(i==0):
		continue
	dur = df["timestamp"][i] - df["timestamp"][i-1]
	if (dur>30):		
		for j in range(30,dur,30):
			k=df.shape[0]
			df.loc[k] = df.iloc[i]
			df.loc[k,'timestamp']-=j
			tt = df.loc[k,'timestamp']
			ss = tt%60
			tt = tt//60
			mm = tt%60
			hh = (tt//60)%24
			df.loc[k,'Time [hh:mm:ss]'] = str(hh)+':'+str(mm)+':'+str(ss)
			# df.loc[k,'DurationCalc'] = dur
	# df["DurationCalc"][i] = dur
df = df.sort_values(by=['timestamp']).reset_index(drop=True)
df.timestamp-=df["timestamp"][0]

# problemdf = df.loc[df["DurationCalc"]!=30]
# df = df.drop(['DurationCalc'], axis=1)
df.to_csv("clean_nfle"+str(ver)+".csv",index=False)

problemdf.head()

##########################           PART TWO            ##########################
"""
repeat = 256
df2 = pd.DataFrame(columns=["Sleep_Stage"],index=range(df.iloc[dataSize-1,6]))
isum=0
for i in range(dataSize):
	sleep_stage=df.iloc[i,0]

	start=df.iloc[i,5]
	end=df.iloc[i,6]

	start=df.iloc[i,5]
	end=df.iloc[i,6]

	df2.loc[start:end]=str(sleep_stage)
"""
