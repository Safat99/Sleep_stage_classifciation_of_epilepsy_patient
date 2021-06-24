from mne import  concatenate_raws
from mne.io import read_raw_edf


raw = read_raw_edf('nfle.edf')
sampling_rate = raw.info['sfreq']
raw_ch_df = raw.to_data_frame(scaling_time =100.0)