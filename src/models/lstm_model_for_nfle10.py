from numpy.lib.twodim_base import tril_indices
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.layers import LSTM, Dense
from tensorflow import keras
from tensorflow.keras import layers, optimizers
from datetime import date, datetime

from tensorflow.python.keras.backend import categorical_crossentropy

# from tensorflow.compat.v1 import ConfigProto
# from tensorflow.compat.v1 import InteractiveSession

# config = ConfigProto()
# config.gpu_options.allow_growth = True
# session = InteractiveSession(config=config)


df = pd.read_csv('nfle_reshaped_final_dataset.csv')
df = df.head(10)

def prepare_dataset(test_size, validation_size):

    features = df.iloc[:,:7680]
    features = features.values # convert df into numpy array for model
    # features = features.reshape(982,7680,1)

    targets = np.array(df.targets.tolist())
    #targets = targets.reshape(982,1)

    le = LabelEncoder() 
    targets = le.fit_transform(targets)

    # le = LabelEncoder() 
    # targets = keras.utils.to_categorical(le.fit_transform(targets))

    #creating train test split
    X_train, X_test, y_train, y_test = train_test_split(features,targets, test_size = 0.25)

    #create validation (not sure is this mnandatory or not)
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size = 0.2)

    X_train = X_train[...,np.newaxis]
    X_test  = X_test[...,np.newaxis]
    X_validation  = X_validation[...,np.newaxis]


    return  X_train, X_validation, X_test, y_train, y_validation, y_test


def build_model():

    model = keras.Sequential()
    #model.add(layers.Embedding(input_dim=input_shape,output_dim=7))
    model.add(LSTM(64, input_shape =(7680,1) ,return_sequences=False))
    # model.add(Dense(7680, activation='relu', input_shape = (7680,1)))
    model.add(layers.Dropout(0.3))    

    model.add(Dense(7, activation = 'softmax'))
    print('build model done!\n')
    
    optimizer = keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer= optimizer, loss = 'sparse_categorical_crossentropy',metrics = ['accuracy'])
    
    model.summary()

    return model

'''def compile_model():
    optimizer = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer= optimizer, loss = 'categorical_crossentropy',metrics = ['accuracy'])
'''

def train_model(model,X_train, X_validation, X_test, y_train, y_validation, y_test):
    start_time = datetime.now()
    model = model
    H = model.fit(x=X_train, y=y_train,  epochs = 5, verbose = 1 )
    # validation_data= (X_validation, y_validation),
    duration = datetime.now() - start_time
    print('Duration for training {}'.format(duration))
    print()
    print('evaluation started also\n')

    test_error, test_accuracy = model.evaluate(X_test, y_test, verbose =1)
    print("Accuracy on test set is : {}". format(test_accuracy))
    print("Error on test set is : {}". format(test_error))

    return H

if __name__ == '__main__':
    
    X_train, X_validation, X_test, y_train, y_validation, y_test = prepare_dataset(0.25,0.2)
    model = build_model()
    print(y_train.shape)
    print(X_train.shape)
    model.fit(x=X_train, y=y_train)

    # H = train_model(model, X_train, X_validation, X_test, y_train, y_validation, y_test)
    # print(X_train.shape)
    # print(X_train[:10])
