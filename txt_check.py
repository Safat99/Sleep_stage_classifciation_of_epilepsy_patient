import pandas as pd

# nfle10 = pd.read_csv('nfle10 .csv')
nfle10  = pd.read_csv('nfle10.csv',delimiter='\t')
del nfle10['Position']
count = 0
faltu = 0
not_included = []
included = []

for i,j in enumerate(nfle10.Time):
	if j.split(':')[2] == '31' or j.split(':')[2] == '01':
		faltu +=1
		included.append(nfle10.iloc[i,:])
		if (nfle10.Location[i] != 'ROC-LOC'):
			count = count + 1
			not_included.append(nfle10.iloc[i,:])

df = pd.DataFrame(not_included)
df1 = pd.DataFrame(included)
print(faltu)
print(count)
print(df)
# print(df1)

# recount =0
# doubled = []
# for i in range(len(nfle10.Time)-1):
# 	if nfle10['Time'][i] == nfle10['Time'][i+1]:
# 		# print(nfle10.iloc[i,:])
# 		# print(nfle10.iloc[i+1,:])
# 		# print()
# 		doubled.append(nfle10.iloc[i,:])
# 		doubled.append(nfle10.iloc[i+1,:])
# 		recount+=1
# print(recount)
# df2 = pd.DataFrame(doubled)
# print(df2)
# print(df2.shape)
