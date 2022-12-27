from __future__ import print_function
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense,Dropout, Activation
from keras.layers import Conv2D,MaxPooling2D, GlobalMaxPooling2D, BatchNormalization

batch_size=32
num_classes=10
data_augmentation=True

(x_train,y_train),(x_test,y_test)=cifar10.load_data()
print('x_train shape',x_train.shape)
print('train samples',x_train.shape[0])
print('test samples',y_train.shape[0])
print(y_train)
print('-------')
pritn(y_test)

y_train=keras.utils.to_categorical(y_train,num_classes)
y_test=keras.utils.to_categorical(y_test,num_classes)

# x_train=x_train.
print(y_train,y_test)