import os, fnmatch
import pandas as pd
import h5py
import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.models import load_model, model_from_json
import scipy.misc

# dimensions of our images.
img_width, img_height = 150, 150

file_names = []
predictions = []

model = model_from_json(open('cats_dogs_architecture.json').read())
model.load_weights('complete_model_weights.h5')

jpg_match_string = '*.jpg'

test_data_dir = './data/test/'

for file in os.listdir(test_data_dir):
  if fnmatch.fnmatch(file, jpg_match_string):
    file_names.append(file)

    img = image.load_img(test_data_dir + file, False, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = x.reshape((1,3,img_width, img_height))
    pred = model.predict(x)
    print file
    print pred[0][0]
    predictions.append(pred[0][0])

submission = pd.DataFrame()
submission['id'] = file_names
submission['id'] = submission['id'].str.replace('.jpg', '')
submission['label'] = predictions
submission.loc[submission['label'] < .001, 'label'] = 0
submission.to_csv('submission.csv', index=False)