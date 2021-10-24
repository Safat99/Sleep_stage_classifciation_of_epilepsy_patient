# this code is for finding mean of 5 nfle patients annotations and mean their bar graph
import matplotlib.pyplot as plt
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-v1', '--version1', required=True, help='version means nfle(10).. so 10 it is')
ap.add_argument('-v2', '--version2', required=True, help='version means nfle(10).. so 10 it is')
ap.add_argument('-v3', '--version3', required=True, help='version means nfle(10).. so 10 it is')
ap.add_argument('-v4', '--version4', required=True, help='version means nfle(10).. so 10 it is')
ap.add_argument('-v5', '--version5', required=True, help='version means nfle(10).. so 10 it is')
args = vars(ap.parse_args())

version1=args['version1']
version2=args['version2']
version3=args['version3']
version4=args['version4']
version5=args['version5']

df1 = pd.read_csv('annotations/clean_nfle'+str(version1)+'.csv')
df2 = pd.read_csv('annotations/clean_nfle'+str(version2)+'.csv')
df3 = pd.read_csv('annotations/clean_nfle'+str(version3)+'.csv')
df4 = pd.read_csv('annotations/clean_nfle'+str(version4)+'.csv')
df5 = pd.read_csv('annotations/clean_nfle'+str(version5)+'.csv')



df1=df1['Sleep Stage']
df2=df2['Sleep Stage']
df3=df3['Sleep Stage']
df4=df4['Sleep Stage']
df5=df5['Sleep Stage']

data = pd.concat([df1,df2,df3,df4,df5],axis=0).reset_index(drop=True)
data = data.value_counts().sort_index()

y=[j/5 for i,j in data.items()]

plt.bar(list(data.keys()),y)
for i,j in enumerate(y):
    plt.text(i,j,str(str('{:.2f}'.format(j*30/3600))+ ' hrs'), va='bottom') 
plt.title('Average Sleep Stages for 5 NFLE people')
plt.savefig('annotations/Average Sleep Stages for 5 NFLE people.pdf')
plt.show()