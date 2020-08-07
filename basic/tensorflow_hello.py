# First, should install conda (check options env var)
# Second, update env and create virtual env
# > conda update -n base conda
# > conda --all
# > python -m pip install --upgrade pip
# > conda create -n tensorflow python=3.6
# > conda activate tensorflow
# Third, install tensorflow v1.5
# > (tensorflow) > pip install tensorflow==1.5
# Other Third, install tensorflow by conda
# > (tensorflow) > conda install tensorflow

import tensorflow as tf

print('# Start')

hello = tf.constant('Hello Tensorflow')

# Same code
# session = tf.Session()
# print(session.run(hello))
# session.close()
with tf.Session() as session:
	print(session.run(hello))

print('# End')