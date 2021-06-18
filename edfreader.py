import pyedflib
import numpy as np
import matplotlib.pyplot as plt


#file_name = pyedflib.data.get_generator_filename()
#f = pyedflib.EdfReader(file_name)
f = pyedflib.EdfReader('./nfle10.edf')
n = f.signals_in_file

signal_labels = f.getSignalLabels()
sigbufs = np.zeros((n, f.getNSamples()[0]))

fig = plt.figure()
ax = plt.axes()

for i in np.arange(n):
    sigbufs[i, :] = f.readSignal(i)
    ax.plot(f.readSignal(i))
    plt.show()