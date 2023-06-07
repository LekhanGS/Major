# -*- coding: utf-8 -*-
"""Vggg14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J6snwb0vWrPLoeyQ60ZhZ4GzUghE1oO7
"""

noimport tensorflow as tf
physical_device = tf.config.experimental.list_physical_devices('GPU')
print("Num GPUs Available: ", len(physical_device))
tf.config.experimental.set_memory_growth(physical_device[0], True)

import tensorflow as tf
physical_devices = tf.config.experimental.list_physical_devices('GPU')
print(physical_devices)
if physical_devices:
  tf.config.experimental.set_memory_growth(physical_devices[0], True)

pip install Keras-Preprocessing

import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras_preprocessing.image import ImageDataGenerator
import numpy as np
import time
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image

os.getcwd()

from google.colab import drive
drive.mount('/content/drive')

cd /content/drive/MyDrive/Malware Dataset/Binary/48240 Malware dataset

os.listdir()

cd /content/drive/MyDrive/Malware Dataset/Binary/48240 Malware dataset/NormalImages

Normal_path='/content/drive/.shortcut-targets-by-id/1_MI4Fow8gZP92vd1d4tffeI_SrP0EbaD/Malware Dataset/Binary/48240 Malware dataset/NormalImages'

Malicious_image_path='/content/drive/.shortcut-targets-by-id/1_MI4Fow8gZP92vd1d4tffeI_SrP0EbaD/Malware Dataset/Binary/48240 Malware dataset/MaliciousImages'

class_1=Malicious_image_path

img_lis=os.listdir(Malicious_image_path)
print("Total Number Of Images in Malicious Class is",len(img_lis))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

fig,axes=plt.subplots(1,5,figsize=(30,10))
for i in range(0,5):
  path=Malicious_image_path+'/'+img_lis[i]
  image=mpimg.imread(path,0)
  axes[i].set_title('Malicious')
  axes[i].axis('off')
  axes[i].imshow(image)

class_0=Normal_path

Ma_img_lis=os.listdir(Normal_path)
print("Total Number Of Images in Normal Class is",len(Ma_img_lis))

from PIL import Image

fig,axes=plt.subplots(1,5,figsize=(30,10))
for i in range(0,5):
  path=Normal_path+'/'+Ma_img_lis[i]
  image=mpimg.imread(path,0)
  # To read the size of image
  im = Image.open(path)
  #print(im.size)
  axes[i].set_title('Normal')
  axes[i].axis('off')
  axes[i].imshow(image)

import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator

print(tf. __version__)

import os
import numpy as np
import shutil
import random

# creating train / val /test
root_dir = '/content/drive/.shortcut-targets-by-id/1_MI4Fow8gZP92vd1d4tffeI_SrP0EbaD/Malware Dataset/'
new_root = 'AllDatasets/'
classes = ['NormalImages', 'MaliciousImages']

for cls in classes:
    os.makedirs(root_dir + new_root+ 'train/' + cls)
    os.makedirs(root_dir +new_root +'val/' + cls)
    os.makedirs(root_dir +new_root + 'test/' + cls)
    
## creating partition of the data after shuffeling

for cls in classes:
    src = root_dir +'/Binary/48240 Malware dataset/'+ cls # folder to copy images from
    print(src)

    allFileNames = os.listdir(src)
    np.random.shuffle(allFileNames)

    ## here 0.75 = training ratio , (0.95-0.75) = validation ratio , (1-0.95) =  
    ##training ratio  
    train_FileNames,val_FileNames,test_FileNames = np.split(np.array(allFileNames),[int(len(allFileNames)*0.70),int(len(allFileNames)*0.80)])

    # #Converting file names from array to list

    train_FileNames = [src+'/'+ name for name in train_FileNames]
    val_FileNames = [src+'/' + name for name in val_FileNames]
    test_FileNames = [src+'/' + name for name in test_FileNames]

    print('Total images  : '+ cls + ' ' +str(len(allFileNames)))
    print('Training : '+ cls + ' '+str(len(train_FileNames)))
    print('Validation : '+ cls + ' ' +str(len(val_FileNames)))
    print('Testing : '+ cls + ' '+str(len(test_FileNames)))
    
    ## Copy pasting images to target directory

    for name in train_FileNames:
      shutil.copy(name, root_dir + new_root+'train/'+cls )


    for name in val_FileNames:
      shutil.copy(name, root_dir +new_root+'val/'+cls )


    for name in test_FileNames:
      shutil.copy(name,root_dir + new_root+'test/'+cls )

os.getcwd()

train_path = '/content/drive/.shortcut-targets-by-id/1_MI4Fow8gZP92vd1d4tffeI_SrP0EbaD/Malware Dataset/AllDatasets/train'
test_path = '/content/drive/.shortcut-targets-by-id/1_MI4Fow8gZP92vd1d4tffeI_SrP0EbaD/Malware Dataset/AllDatasets/test'
valid_path = '/content/drive/.shortcut-targets-by-id/1_MI4Fow8gZP92vd1d4tffeI_SrP0EbaD/Malware Dataset/AllDatasets/val'

datagen = ImageDataGenerator(rotation_range =30,
                             shear_range = 0.06,
                             zoom_range = 0.06,
                             samplewise_center=True,
                             samplewise_std_normalization= True,
                             width_shift_range=0.06,
                             height_shift_range=0.06,
                             fill_mode='nearest',
                             horizontal_flip=True,
                             vertical_flip=True, rescale=1./255
                             )

train_data = datagen.flow_from_directory(directory = train_path,
                                         target_size =(128, 128),
                                         classes = ['MaliciousImages','NormalImages'],
                                         batch_size = 32 )


val_data = datagen.flow_from_directory(directory = valid_path,
                                       target_size =(128, 128),
                                       classes = ['MaliciousImages','NormalImages'],
                                       batch_size = 32 )



test_data = datagen.flow_from_directory(directory = test_path,
                                       target_size =(128, 128),
                                       classes = ['MaliciousImages','NormalImages'],
                                       batch_size = 32,
                                       shuffle = False)

def VGG16():

  input = tf.keras.layers.Input(shape=(128, 128, 3))
  
  conv1 = tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(input)
  conv2 = tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(conv1)
  pool1 = tf.keras.layers.MaxPooling2D((2, 2), (2,2))(conv2)
  conv3 = tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(pool1)
  conv4 = tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(conv3)
  pool2 = tf.keras.layers.MaxPooling2D((2, 2), (2,2))(conv4)
  conv5 = tf.keras.layers.Conv2D(256, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(pool2)
  conv6 = tf.keras.layers.Conv2D(256, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(conv5)
  conv7 = tf.keras.layers.Conv2D(256, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(conv6)
  pool3 = tf.keras.layers.MaxPooling2D((2, 2), (2,2))(conv7)
  conv8 = tf.keras.layers.Conv2D(512, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(pool3)
  conv9 = tf.keras.layers.Conv2D(512, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(conv8)
  conv10 = tf.keras.layers.Conv2D(512, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(conv9)
  pool4 = tf.keras.layers.MaxPooling2D((2, 2), (2,2))(conv10)
  conv11 = tf.keras.layers.Conv2D(512, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(pool4)
  conv12 = tf.keras.layers.Conv2D(512, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(conv11)
  conv13 = tf.keras.layers.Conv2D(512, kernel_size=(3, 3), activation='relu', padding='same', kernel_initializer='he_normal')(conv12)
  pool5 = tf.keras.layers.MaxPooling2D((2, 2), (2,2))(conv13)


  dense1 = tf.keras.layers.Dense(4096, activation='relu')(pool5)
  dense2 = tf.keras.layers.Dense(4096, activation='relu')(dense1)
  global_pool = tf.keras.layers.GlobalAveragePooling2D()(dense2)
  output = tf.keras.layers.Dense(2, activation='sigmoid')(global_pool)
  
  model = tf.keras.models.Model(inputs=input, outputs=output)
  return model
model= VGG16()

model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

from PIL import Image

model.fit(x=train_data, validation_data= val_data, epochs=10, verbose=2)

test_imgs, test_labels = next(test_data)

test_data.classes

predictions = model.predict(x = test_data, verbose = 0)

np.round(predictions)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_true=test_data.classes, y_pred = np.argmax(predictions,axis = -1))

def plot_confusion_matrix(cm, classes,
                         normalize=False,
                         title='Confusion Matrix',
                         cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap = cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation = 90)
    plt.xticks(tick_marks, classes)
    
    
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix, without normalization")
        
    print(cm)
    
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                horizontalalignment = "center",
                color="white" if cm[i, j ] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

import itertools

cm_plot_labels = ['Malicious', 'Normal']

test_data.class_indices

plot_confusion_matrix(cm=cm, classes = cm_plot_labels, title='Confusion Matrix')

accuracy = (cm[0][0] + cm[1][1])/(sum(sum(cm)))
print('Accuracy:', accuracy)

precision = (cm[0][0])/(sum(cm)[0])
print('Precision:',precision)

recall = (cm[0][0])/sum(cm[0])
print('Recall:', recall)

f_one_score = 2 * (precision*recall)/(precision + recall)
print('F1 Score:',f_one_score)


p1 = sum(cm[0])/sum(sum(cm))
p2 = sum(cm)[0]/sum(sum(cm))
random_accuracy = p1*p2 + (1-p1)*(1-p2)

kappa = (accuracy - random_accuracy)/(1 - random_accuracy)
print('Kappa', kappa)