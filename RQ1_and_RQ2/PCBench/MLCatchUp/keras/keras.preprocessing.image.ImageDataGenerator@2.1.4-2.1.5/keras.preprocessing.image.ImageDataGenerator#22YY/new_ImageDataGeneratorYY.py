from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False, False, False, False, False, 1e-06, brightness_range=None, validation_split=0.0)
