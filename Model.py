import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, LSTM, Reccurent2D



model = Sequential()
model.add(LSTM('''add details here'''))
model.add(Dropout(0.15))
model.add(Conv2D('''details'''))
model.add(Dense(128))
model.add(Dropout(0.15))
model.add(Flatten())
model.add(Dense(128))
model.add(Flatten())

model.compile(optimizer = adam)
model.fit()
