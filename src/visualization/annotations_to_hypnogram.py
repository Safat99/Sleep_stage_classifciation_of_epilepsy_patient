import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import argparse
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('-v', '--version', required=True, help='version means nfle(10).. so 10 it is')
args = vars(ap.parse_args())



version = args['version']
Path('assets/bar_graphs').mkdir(parents=True, exist_ok=True)
Path('assets/hypnograms').mkdir(parents=True, exist_ok=True)

df = pd.read_csv('annotations/clean_nfle'+str(version)+'.csv')
df = df['Sleep Stage']

## if i wanna view the annotations 
# print(df.describe())
# print(df.unique())
# print(df.value_counts())

## for plotting bar graphs 
data = df.value_counts()
y = [j for i,j in data.items()]
plt.bar(list(data.keys()), y)
for i,j in enumerate(y):
    plt.text(i,j,str(str('{:.2f}'.format(j*30/3600))+ ' hrs'), va='bottom') 
plt.savefig('assets/bar_graphs/nfle{}_bar_graph.png'.format(version), bbox_inches='tight')




hypno_dict = {'W':6 , 'R':5, 'S1':4, 'S2':3, 'S3':2, 'S4':1}
hypno_df = df.map(lambda x : hypno_dict[x])


x = np.arange(len(hypno_df)) * 30 / 3600
yy = ['S4', 'S3', 'S2', 'S1', 'REM', 'WAKE']

plt.style.use('ggplot')
plt.figure(figsize=(10.24,5.78))

ax =plt.plot(x,hypno_df)



# plt.yticks(hypno_df,yy)
# ax.set(yticks=yy)
plt.title('Hypnogram for nfle{}'.format(version))
plt.xlabel('Time(hrs)')
plt.ylabel('Sleep Stage')
plt.yticks(list(range(1,7)),labels=yy)
plt.savefig('assets/hypnograms/nfle{}_hypnogram.png'.format(version), bbox_inches='tight')
plt.show()