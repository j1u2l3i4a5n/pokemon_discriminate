# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 07:13:09 2019

@author: Peter Wang
"""

from keras.models import Sequential  #用來啟動 NN
from keras.layers import Conv2D  # Convolution Operation
from keras.layers import MaxPooling2D # Pooling
from keras.layers import Flatten
from keras.layers import Dense # Fully Connected Networks
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils

import numpy as np
import pandas as pd
import random

def train_test_split(images, labels, poke_dic):
    currenct_poke = ''
    choice_list = []
    test_labels = []
    for index, value in enumerate(labels['name']):
        if value == currenct_poke:
            choice_list.append(index)
        else:
            if choice_list:
                test_labels.append(random.choice(choice_list))
            currenct_poke = value
            choice_list = []
            choice_list.append(index)
            
    train_images = []
    test_images = []  
    train_id = []
    test_id = []
    for index, image in enumerate(images):    
        if index in test_labels:
            test_images.append(image)
            test_id.append(poke_dic[labels['name'][index]])
        else:
            train_images.append(image)
            train_id.append(poke_dic[labels['name'][index]])
    return  np.array(train_images), np_utils.to_categorical(train_id), np.array(test_images), np_utils.to_categorical(test_id)
images = np.load('poke_image_data.npy')
images = images / 255
n, width, length, color_num = images.shape
labels = pd.read_csv('names_and_strengths.csv')
names, strength = labels['name'], labels['strength']
kinds = len(set(names))
name_list = list(set(names))
name_dict = dict(zip(name_list,range(len(name_list))))
'''
'''
name_id = []
for i in names:
    name_id.append(name_dict[i])
name_one_hot = np_utils.to_categorical(name_id)
'''

'''
train_x, train_y, test_x, test_y = train_test_split(images, labels, name_dict)
train_imgen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)
test_imgen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)
train_imgen.fit(train_x)
test_imgen.fit(test_x)
#data = preprocess.read_files('data/ace', split_half=True)
#data2 = preprocess.read_files('data/titan/', split_half=False)
#ace = preprocess.read_files_name('data/ace', lable='ace')
#titan = preprocess.read_files_name('data/titan', lable='titan')
#
#data_merge = ace + titan



google_gen = ImageDataGenerator(
    featurewise_center=True,
    featurewise_std_normalization=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    fill_mode = 'constant'
)


model = Sequential()  
model.add(Conv2D(32, (5, 5), strides = 3, input_shape = (100, 100, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(64, (5, 5), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

# Third convolutional layer
model.add(Conv2D(128, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(output_dim = 806, activation = 'relu'))
model.add(Dense(output_dim = 806, activation = 'relu'))
model.add(Dense(output_dim = 806, activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
model.summary()

model.fit_generator(generator=google_gen.flow_from_directory('data/pokemon_npy_png_test', target_size=(100, 100), color_mode='rgb'), 
                    validation_data=google_gen.flow_from_directory('data/pokemon_npy_png_train', target_size=(100, 100), color_mode='rgb'), 
                    steps_per_epoch=3000,
                    validation_steps=300, 
                    epochs = 20
                    )
model.save('pokemon_classifer_BC.h5')