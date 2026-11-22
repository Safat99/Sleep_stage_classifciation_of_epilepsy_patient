import  pandas as pd

left = pd.read_csv('left.csv')
right = pd.read_csv('rht.csv')

left['Sleep_Stage'] = right.head(len(left))
left.to_csv('nfle10_dataset.csv', index=False)

