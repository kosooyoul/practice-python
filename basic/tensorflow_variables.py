import tensorflow as tf

print('# Start')

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = a + b

feed1 = {a: 1.0, b: 3.0}
feed2 = {a: [1.0, 2.0], b: [3.0, 4.0]}

with tf.Session() as session
	print(session.run(c, feed_dict = feed1))
	print(session.run(c, feed_dict = feed2))

	d = c ** 2

	print(session.run(d, feed_dict = feed1))
	print(session.run(d, feed_dict = feed2))

print('# End')