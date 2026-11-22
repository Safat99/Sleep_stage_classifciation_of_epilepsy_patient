# https://bigdatawg.nist.gov/HackathonTutorial.html

import mne
from mne.io import read_raw_edf
from mne.transforms import scaling

mne.set_log_level('Warning')
raw = read_raw_edf('nfle10.edf')

# print(len(raw))

print(raw.info)

# # Get the sample rate
sfreq = raw.info['sfreq']
# print('Sample rate:', raw.info['sfreq'], 'Hz')

print(raw.info['channel_names'])


# Get the size of the matrix
# print('Size of the matrix: {}\n'.format(raw.get_data().shape))

#if I wanna plot and see the sensors
fig = raw.plot()

## with matplotlib pyplt I can visualise specific channels graph
import matplotlib.pyplot as plt
raw_specific = raw.to_data_frame(scalings=100)[['ROC-LOC','FP2-F4', 'F4-C4', 'F7-T3', 'F3-C3', 'T4-T6']]

