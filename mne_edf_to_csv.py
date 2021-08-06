import mne
from mne.io import read_raw_edf
from mne.transforms import scaling
import pandas as pd
from datetime import datetime

mne.set_log_level('Warning')
raw = read_raw_edf('nfle10.edf')

start = datetime.now()
df = raw.to_data_frame(scalings=100.0)[['ROC-LOC','FP2-F4', 'F4-C4', 'F7-T3', 'F3-C3', 'T4-T6']]
#[['ROC-LOC','Fp2-F4', 'F4-C4', 'F7-T3', 'F3-C3', 'T4-T6']]
#print(df)
#['FP2-F4', 'F4-C4', 'C4-P4', 'P4-O2', 'F8-T4', 'T4-T6', 'FP1-F3', 'F3-C3', 'C3-P3', 'P3-O1', 'F7-T3', 'T3-T5', 'C4-A1']
end1 = datetime.now()
print(end1-start)

df.to_csv('nfle10_more_sensor_values.csv',index=False)
end2 = datetime.now()
print(end2-end1)
