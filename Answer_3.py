import h5py
import numpy as np
import pandas as pd
import csv
import scipy.signal as m
import matplotlib.pyplot as plt

f = h5py.File("/home/prathamesh/Desktop/CERN_work/Cern_work/data.h5", 'r')
variable_path = f['AwakeEventData']['XMPP-STREAK']['StreakImage'] # Reading the data giving the required path 
imageData = variable_path['streakImageData']
imageHeight = variable_path['streakImageHeight']
imageWidth = variable_path['streakImageWidth']
imageArray = np.reshape(imageData, (imageHeight[0], imageWidth[0])) # Reshaping the data to 2D array

image = m.medfilt(imageArray) # Filtering the image 2D array

# Plotting and saving the image
plot = plt.imshow(img) 
plt.imsave("task.png", img)
