import h5py
import numpy as np
import pandas as pd
import csv

def extract(name, dataset):
  if isinstance(dataset, h5py.Dataset): # If a dataset is caught then the following is stored in the CSV file.
    try:
     value = [dataset.name, dataset.shape, dataset.size, dataset.dtype]
     writer.writerow(value) 
    except:
      pass

with open("/home/prathamesh/Desktop/CERN_work/Cern_work/file.csv", "w") as file_to_write: 
       f = h5py.File("/home/prathamesh/Desktop/CERN_work/Cern_work/data.h5", 'r')
       writer = csv.writer(file_to_write)
       title = ['name', 'size', 'shape', 'type'] # Creating the initial column index
       writer.writerow(title)
       f.visititems(extract) # Calling the data of hdf5 file recursively
    
