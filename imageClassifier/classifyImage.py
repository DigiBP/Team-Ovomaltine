import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model

def load_and_preprocess_data(img):
    data = []

    img = keras.preprocessing.image.load_img(img, target_size=(150,150))
    img_array = keras.preprocessing.image.img_to_array(img)


    data = np.array(img_array)

    return data

def classifyImage(image):
    new_image = load_and_preprocess_data(image)
    
    
    model = load_model('imageClassifier/breast_cancer_classifier_model.keras')
    
    result = model.predict(np.expand_dims(new_image, axis=0))
    class_names = ["benign", "malignant"]
    prediction = class_names[int(np.round(result[0]))]
    

    return prediction

if __name__ == "__main__":

    img = "imageClassifier/SOB_B_A-14-22549G-40-001.png"
    result = classifyImage(img)
    class_names = ["benign", "malignant"]
    print(class_names[int(np.round(result[0]))])