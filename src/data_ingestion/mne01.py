import mne
from mne.io import read_raw_edf

mne.set_log_level('WARNING') #output becomoes less verbose

raw = read_raw_edf('nfle10.edf')
print(raw)

raw.filter(1.,40., n_jobs = 1)  #band pass filter >> ei freq er moddher gula true
#eta terminal e kaaj kore nai>> onek boro time er ejonno hote paare

print(raw.info) #onek info show kore >> notebook better

fig = raw.plot()


