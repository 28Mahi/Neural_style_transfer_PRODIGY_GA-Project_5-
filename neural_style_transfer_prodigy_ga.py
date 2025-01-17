# -*- coding: utf-8 -*-
"""Neural_style_transfer_PRODIGY_GA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lnzPatQsU7gPDv2VaRuiclLvRC-aUQoQ

# Importing the Dependencies
"""

import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

"""# Preprocess Image and Load"""

def load_image(img_path):
  img = tf.io.read_file(img_path)
  img = tf.image.decode_image(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)
  img = img[tf.newaxis, :]
  return img

content_image = load_image('/Screenshot 2023-11-12 164138.png')
style_image = load_image('/Screenshot (9).png')

"""# Visualize Output"""

plt.imshow(np.squeeze(content_image))
plt.title("Content Image")
plt.show()

plt.imshow(np.squeeze(style_image))
plt.title("Style Image")
plt.show()

"""# Output Image"""

stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

plt.imshow(np.squeeze(stylized_image))
plt.title("Stylized Image")
plt.show()