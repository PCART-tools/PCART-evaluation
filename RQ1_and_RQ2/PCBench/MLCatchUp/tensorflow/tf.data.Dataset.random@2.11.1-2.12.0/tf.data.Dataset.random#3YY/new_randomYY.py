import tensorflow as tf
ds1 = tf.data.Dataset.random(seed=4).take(10, rerandomize_each_iteration=None)
