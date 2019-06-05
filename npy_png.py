# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:59:47 2019

@author: rjlin
"""

import os
import numpy as np
from PIL import Image
import random

def npy_to_png(path_npy, path_png_train, path_png_test, split_ratio=0.2):
    npy_path = os.listdir(path_npy)
    png_path_train = os.listdir(path_png_train)
    png_path_test = os.listdir(path_png_test)
    
    for i in npy_path:
        label = i[:-4]
        images = np.load(path_npy + '/' + i)        
        im_num = images.shape[0]
        im_index = list(range(im_num))
        random.shuffle(im_index)
        for index, value in enumerate(im_index):
            image = (images[value] * 255).astype('uint8')
            im = Image.fromarray(image)
            if index <= im_num*split_ratio:
                if not label in png_path_test:
                    os.mkdir(path_png_test + '/' + label)
                    png_path_test.append(label)
                im.save("%s/%s/%s.png"%(path_png_test, label, index))
            else:
                if not label in png_path_train:
                    os.mkdir(path_png_train + '/' + label)
                    png_path_train.append(label)
                im.save("%s/%s/%s.png"%(path_png_train, label, index))

if __name__ == '__main__':
    npy_to_png('data/pokemon_google_data', 'data/pokemon_npy_png_train', 'data/pokemon_npy_png_test')