import sys
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.metrics import classification_report
from keras.models import load_model
# import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from cv2 import resize, INTER_AREA, INTER_CUBIC
from flask import Flask, request,jsonify,render_template,redirect,url_for, session
import os
import json
from json import JSONEncoder
import io
import random


app = Flask(__name__)
app.secret_key="1234"
def get_model():
    global model
    filename = 'gamma_hadron_model.sav'
    model = pickle.load(open(filename, 'rb'))
    print(" * Model loaded!")

def preprocess_image(image):
    image = image.reshape((1, *image.shape))
    return image

print(" * Loading Keras model...")
get_model()


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":        
        if request.files:
            raw_data = request.files['image'].read()         
            finalNumpyArray=np.array(json.loads(raw_data), dtype = 'float')
            processed_image = preprocess_image(finalNumpyArray)
            prediction = model.predict_proba(processed_image).tolist()

            response ={
                    'Gamma': str(round(100*prediction[0][0], 3)) + ' %',
                    'Hadron': str(round(100*prediction[0][1], 3)) + ' %',
                }    
            # breakpoint()
            return render_template('predict copy.html',prediction=response)
    return render_template('semiconui copy.html')

@app.route('/predict/',methods=['GET','POST'])
def predict():
    if "response" in session:
        prediction=session['response']
        return render_template('predict copy.html', prediction=prediction)
    else:
        return redirect(url_for('index'))

    

if __name__ == '__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)