import numpy as np
import pandas as pd

df = pd.read_csv('nfle10_more_sensor_values.csv')
df = df.iloc[230400:7534080,:] # 930s * 256 frame
df = df.reset_index(drop=True)
print(df.head(5))
print(df.shape)

# roc_loc = df['ROC-LOC'].values
# fp2_f4 = df['FP2-F4'].values
# f4_c4 = df['F4-C4'].values
# f7_t3 = df['F7-T3'].values
# f3_c3 = df['F3-C3'].values
# t4_t6 = df['T4-T6'].values

# roc_loc = np.reshape(roc_loc,(952,7680))
# fp2_f4 = np.reshape(fp2_f4,(952,7680))

# arr = np.stack((roc_loc, fp2_f4),axis=1)

ch = {} # empty dict
for i in df.columns:
    ch[i] = df[i].values
    ch[i] = np.reshape(ch[i], (951,7680))

arr = np.stack([i for i in ch.values()],axis=1)