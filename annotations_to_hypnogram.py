import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

version = 10
df = pd.read_csv('clean_nfle10.csv')
df = df['Sleep Stage']

## if i wanna view the annotations 
# print(df.describe())
# print(df.unique())
# print(df.value_counts())

## for plotting bar graphs 
data = df.value_counts()
y = [j for i,j in data.items()]
plt.barh(list(data.keys()), y)
for i,j in enumerate(y):
    plt.text(j,i,str(str('{:.2f}'.format(j*30/3600))+ ' hrs')) 
plt.savefig('annotations/nfle{} bar graph'.format(version))




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
plt.savefig('annotations/nfle{} hypnogram'.format(version))
plt.show()