import pandas as pd
import numpy as np

df = pd.read_csv('nfle10_dataset.csv')
df1 = df.iloc[:,0]
df1 = df1.values
df1 = df1.reshape(982,7680)
print(df1.shape)
df1 = pd.DataFrame(df1)

df2 = df.Sleep_Stage.values
Sleep_Stages = []
for i in enumerate(df2):
    if i[0] % 7680 == 0:
        Sleep_Stages.append(i[1])

df2 = pd.DataFrame(Sleep_Stages)

df1['targets'] = df2
#print(df1)

df1.to_csv('nfle_reshaped_final_dataset.csv',index=False)