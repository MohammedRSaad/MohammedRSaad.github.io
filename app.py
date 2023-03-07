#import numpy as np
import pandas as pd
from sklearn import preprocessing
from flask import Flask, request, render_template
from keras.models import load_model
from pathlib import Path

THIS_FOLDER = Path(__file__).parent.resolve()
print(THIS_FOLDER)

app = Flask(__name__)
model = load_model(str(THIS_FOLDER / "models/model.h5"))

@app.route('/')
def home():
    return render_template('index.html')
    