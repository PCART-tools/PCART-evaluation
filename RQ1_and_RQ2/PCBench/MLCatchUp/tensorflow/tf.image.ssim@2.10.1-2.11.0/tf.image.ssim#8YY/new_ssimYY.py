import tensorflow as tf
im1 = tf.image.decode_image(tf.io.read_file('/home/zhang/Packages/tensorflow_file/better_last.png'))
im2 = tf.image.decode_image(tf.io.read_file('/home/zhang/Packages/tensorflow_file/better_last.png'))
tf.shape(im1)
tf.shape(im2)
im1 = tf.expand_dims(im1, axis=0)
im2 = tf.expand_dims(im2, axis=0)
ssim1 = tf.image.ssim(im1, img2=im2, max_val=255, filter_size=11, return_index_map=False)
