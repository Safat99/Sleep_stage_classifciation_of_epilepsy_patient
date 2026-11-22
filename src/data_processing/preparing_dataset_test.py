import pandas as pd
import numpy as np

df = pd.read_csv('nfle_reshaped_final_dataset.csv')
features =df.iloc[:,7679].values
print(features)
features = features.reshape(982,1)
targets = np.array(df.targets.tolist())
targets = targets.reshape(982,1)


X_train=[]
y_train=[]


for i in range(50, len(features)): 
    X_train.append(features[i-50:i,0]) #X_raw_train_scaled 
    y_train.append(targets[i,0]) #y_raw_train_scaled
X_train, y_train= np.array(X_train), np.array(y_train) 
type(X_train) 
print(X_train.shape)
print(y_train.shape)