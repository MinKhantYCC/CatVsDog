# CatVsDog

This is Cat Vs Dog Image Classification by using CNN architecture.
The data set for this file can be download from kaggle.

## CNN Architecture
( CONV2D >> BatchNormalization >> MaxPooling2D >> Dropout ) x 3 >>
Flatten >> Dense >> BatchNormalization >> Dropout >> Dense

Since there are a lot of train images (12500,128,128,3), we use generator 
to feed these samples into our model instead of feeding all images at once.

## Result
Need to train nearly 2 Hrs for 10 epochs on Window 11, i3-10th with 8Gb Memory.
Future Work => Test with ResNet50 and MobileNetV2.

## Files Description
CatVsDog-CNN2.ipynb is for model training.
model1_catsVSdogs_10epoch.h5 is my pre-trained model file (output from CatVsDog-CNN2.ipynb)
CatVsDog-GUI.py is used for API with streamlit.