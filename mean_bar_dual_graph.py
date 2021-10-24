import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ver1,ver2,ver3,ver4,ver5 = list(input('Input 5 NFLE patients:\n').split())
# ver1,ver2,ver3,ver4,ver5 = str(39),str(18),str(7),str(21),str(28)


df1 = pd.read_csv('annotations/clean_nfle'+ver1+'.csv')
df2 = pd.read_csv('annotations/clean_nfle'+ver2+'.csv')
df3 = pd.read_csv('annotations/clean_nfle'+ver3+'.csv')
df4 = pd.read_csv('annotations/clean_nfle'+ver4+'.csv')
df5 = pd.read_csv('annotations/clean_nfle'+ver5+'.csv')

df1=df1['Sleep Stage']
df2=df2['Sleep Stage']
df3=df3['Sleep Stage']
df4=df4['Sleep Stage']
df5=df5['Sleep Stage']

data = pd.concat([df1,df2,df3,df4,df5],axis=0).reset_index(drop=True)
data = data.value_counts().sort_index()
y_nfle=[(j/5)*30/3600 for i,j in data.items()]

ver1,ver2,ver3,ver4,ver5 = list(input('Input 5 Normal patients:\n').split())
# ver1,ver2,ver3,ver4,ver5 = str(4),str(10),str(11),str(12),str(13)

df1 = pd.read_csv('annotations/clean_n'+ver1+'.csv')
df2 = pd.read_csv('annotations/clean_n'+ver2+'.csv')
df3 = pd.read_csv('annotations/clean_n'+ver3+'.csv')
df4 = pd.read_csv('annotations/clean_n'+ver4+'.csv')
df5 = pd.read_csv('annotations/clean_n'+ver5+'.csv')

df1=df1['Sleep Stage']
df2=df2['Sleep Stage']
df3=df3['Sleep Stage']
df4=df4['Sleep Stage']
df5=df5['Sleep Stage']

data2 = pd.concat([df1,df2,df3,df4,df5],axis=0).reset_index(drop=True)
data2 = data2.value_counts().sort_index()
y_n=[(j/5)*30/3600 for i,j in data2.items()]

x_axis = np.arange(6)

plt.bar(x_axis - 0.2, y_n, 0.4, label='Normal People')
plt.bar(x_axis + 0.2, y_nfle, 0.4, label='NFLE Patients')
plt.xticks(x_axis,list(data.keys()))


for i,j in enumerate(y_n):
    plt.text(i,j,str(str('{:.2f}'.format(j))+ ' hrs'), va='bottom')

for i,j in enumerate(y_nfle):
    plt.text(i,j,str(str('{:.2f}'.format(j))+ ' hrs'), va='bottom')
     
plt.title('Average Differences of 8 hours Sleep Stages')
plt.xlabel('Sleep Stages')
# plt.ylabel('Number of 30 seconds epochs')
plt.ylabel('Number of sleeping hours (hrs)')
plt.legend()
plt.savefig('annotations/Average Differences of 8 hours Sleep Stages between 5 NFLE and Normal peoples.pdf')
plt.show()

##output
'''
Input 5 NFLE patients:
39 18 7 21 28 
Input 5 Normal patients:
4 10 11 12 13
'''