# -*- coding: utf-8 -*-
"""05b-mle-cameraman.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f-cgUGG_ZWcR5rigA03nfnn_mDv0u6Zb
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import cv2

def process_image(image_path):
    # Read the image as an array
    img_array = cv2.imread(image_path)

    # Convert the image to grayscale and normalize the values between 0 and 1
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY) / 255

    # Set the number of repetitions for the image
    num_repetitions = 100

    # Repeat the grayscale image num_repetitions times along the third axis
    repeated_img = np.repeat(gray_img[:, :, np.newaxis], num_repetitions, axis=2)

    # Generate random values following a Poisson distribution based on the repeated image
    poisson_img = stats.poisson.rvs(repeated_img)

    # Create a binary mask based on a threshold value
    threshold = 1
    binary_mask = (poisson_img >= threshold).astype(float)

    # Estimate the parameter using the binary mask
    estimated_param = -np.log(1 - np.mean(binary_mask, axis=2))

    # Display the estimated parameter as a grayscale image
    plt.imshow(estimated_param, cmap='virdis')
    plt.show()

# Specify the path to the image
img_path = '/content/kids.tif'

# Process the image
process_image(img_path)