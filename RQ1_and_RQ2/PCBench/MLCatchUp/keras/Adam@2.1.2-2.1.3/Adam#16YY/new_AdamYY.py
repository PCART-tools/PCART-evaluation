from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
adam_optimizer = Adam(0.001, 0.9, 0.999, 1e-08, 0.0, amsgrad=False)
