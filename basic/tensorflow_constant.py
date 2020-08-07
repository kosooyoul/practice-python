import tensorflow as tf

print('# Start')

a = tf.constant(1.0, name = 'a')
b = tf.constant(2.0, name = 'b')
c = tf.constant([[1.0, 2.0], [3.0, 4.0]], name = 'c')

print(a)
print(b)
print(c)

with tf.Session() as session:
	print(session.run([a, b]))
	print(session.run(c))
	print(session.run(a + b))
	print(session.run(c * 2 + 1.0))

print('# End')