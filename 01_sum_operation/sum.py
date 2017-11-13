# Simple hello world in tensorflow

import tensorflow as tf

a=tf.constant(10,dtype=tf.float32)
b=tf.constant(20,dtype=tf.float32)

#Tensorflow has overloaded operators, here is how to show it#

sum1=a+b #possible due to object operation being loaded

sum2=tf.add(a,b)

with tf.Session() as sess: #context manager handels this
	print(sess.run(sum1), sess.run(sum2))
	print("Using a+b has same effect as using tf.add(a,b)")