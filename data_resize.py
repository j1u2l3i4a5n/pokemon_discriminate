# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:14:37 2019

@author: rjlin
"""

import os 
import cv2
import numpy as np
from matplotlib.image import imread
from matplotlib import pyplot as plt

image_path1 = os.listdir('downloads/')

for i in image_path1:
    data = []
    image_paths2 = os.listdir('downloads/%s'%i)
    for j in image_paths2:
        try:
            image = imread('downloads/%s/%s'%(i,j))
            if image.shape[2] == 4:
                image = np.delete(image, 3, 2)
            
            image = cv2.resize(image, (100,100))
            if not 'float' in str(image.dtype):
                image = image / 255
                
            data.append(image)
        except:
            try:
                image = cv2.imread('downloads/%s/%s'%(i,j))
                if image.shape[2] == 4:
                    image = np.delete(image, 3, 2)
                    
                image = cv2.resize(image, (100,100))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    

                if not 'float' in str(image.dtype):
                    image = image / 255

                data.append(image)
                
            except Exception as e:
                print(e)
                print(i,j)
            
    data = np.array(data)
    np.save('data/%s.npy'%i, data)
''' 
data_path = os.listdir('data')
 
for i in data_path:
    try:
        matrix = np.load('data/%s'%i)
        if matrix.shape[0] < 20:
            print(i)
            print(matrix.shape)
    except:
        pass
'''