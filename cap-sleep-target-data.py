# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:11:48 2020

@author: Shamim
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
import math 
import cv2
'''
##########################           PART ONE            ##########################



nfle10 = pd.read_csv("nfle10.csv")
dataSize=nfle10.shape[0]
#dataSize = 5
repeat = 256
main_df = pd.DataFrame(columns=["Sleep_Stage"],index=range(nfle10.iloc[dataSize-1,6]))

for i in range(dataSize):
	sleep_stage=nfle10.iloc[i,0]
	start=nfle10.iloc[i,5]
	end=nfle10.iloc[i,6]
	main_df.loc[start:end]=str(sleep_stage)

main_df.to_csv('rht.csv', index = False)

