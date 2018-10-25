import tensorflow as tf
import cv2
import numpy as np


with tf.Session() as sess:
    # load the model trained by mnist_deep.py
    model = tf.train.import_meta_graph("./models/model.ckpt.meta")
    model.restore(sess,"./models/model.ckpt")

    # get the input output keep_prob tensor
    graph = tf.get_default_graph()
    input = graph.get_tensor_by_name('input:0')
    output = graph.get_tensor_by_name('output:0')
    keep_prob = graph.get_tensor_by_name('keep_prob:0')

    # read the eval image
    frame = cv2.imread('1.jpg')
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image_gray_28_28 = cv2.resize(image_gray, (28, 28))

    #format the right shap for input
    data = np.zeros([1, 784], np.float32)
    data[0] = np.array(image_gray_28_28).astype(float).reshape(-1)


    result = sess.run(output, feed_dict={input: (data), keep_prob: 0.5})
    print(result)
    print(tf.argmax(result, 1).eval())
