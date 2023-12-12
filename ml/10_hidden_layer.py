import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math, random

np.random.seed(1000)

function_to_learn = lambda x : np.cost(x) + 0.1*np.random.randn(*x.shape)

layer_1_neurons = 10 
points = 1000
batch_size = 100
epochs = 1500 

# Generate random data
all_x = np.float32(np.random.uniform(-2 * math.pi, 2 * math.pi, (1, points))).T
np.random.shuffle(all_x)

# Train and validation split
train_size = 900
x_training, x_validation = all_x[:train_size], all_x[train_size:]
y_training, y_validation = function_to_learn(x_training), function_to_learn(x_validation)

# Plot the data
plt.scatter(x_training, y_training, c='blue', label='train')
plt.scatter(x_validation, y_validation, c='pink', label='validation')
plt.legend()
plt.show()

# Build the model
X = tf.placeholder(tf.float32, [None, 1], name="X")
Y = tf.placeholder(tf.float32, [None, 1], name="Y")

# Neural network layers
def dense_layer(input_layer, output_size, activation=tf.nn.sigmoid):
    weights = tf.Variable(tf.random.uniform([input_layer.shape[1], output_size], -1, 1, dtype=tf.float32))
    biases = tf.Variable(tf.zeros([1, output_size], dtype=tf.float32))
    return activation(tf.matmul(input_layer, weights) + biases)

h = dense_layer(X, layer_1_neurons)
model = dense_layer(h, 1, activation=lambda x: x)

# Training setup
loss = tf.nn.l2_loss(model - Y)
train_op = tf.train.AdamOptimizer().minimize(loss)

# Start TensorFlow session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Training loop
    errors = []
    for i in range(epochs):
        for start, end in zip(range(0, len(x_training), batch_size), range(batch_size, len(x_training), batch_size)):
            sess.run(train_op, feed_dict={X: x_training[start:end], Y: y_training[start:end]})
        
        cost = sess.run(loss, feed_dict={X: x_validation})
        errors.append(cost)

        if i % 100 == 0:
            print("epoch %d, cost = %g" % (i, cost))

# Plot the training curve
plt.plot(errors, label='MLP Function Approximation')
plt.xlabel('epochs')
plt.ylabel('cost')
plt.legend()
plt.show()