import tensorflow as tf
model = tf.keras.Sequential([tf.keras.layers.Dense(5, input_shape=(3,)), tf.keras.layers.Softmax()])
model.save('/home/zhang/Packages/tensorflow_file', True, include_optimizer=True, save_traces=True)
