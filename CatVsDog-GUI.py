import numpy as np
import pandas as pd
import cv2
import tensorflow as tf
import tensorflow.keras.layers as tfl
from tensorflow.python.framework import ops
import os
import streamlit as stm

from keras.models import load_model
model = load_model('model1_catsVSdogs_10epoch.h5')

img_dir = stm.text_input('Enter Image Directory', '', placeholder='Image Directory')

def classify(img_in):
    lab = model.predict(img_in)
    lab = np.argmax(lab)
    label = 'cat' if lab == 0 else 'dog'
    return label

if img_dir:
    img = cv2.imread(img_dir)
    img_resize = cv2.resize(img, (128,128))
    img_in = np.reshape(img_resize, [1,128,128,3])
    img_in = img_in/255
    stm.image(img)
    state = stm.button('Classify')
    if state:
        label = classify(img_in)
        stm.header('It is a '+ label)
