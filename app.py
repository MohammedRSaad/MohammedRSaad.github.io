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

'''@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
    features = ['BMXWT', 'BMXHT', 'BMXBMI', 'RIDAGEYR', 'MGXH1T1', 'MGXH2T1', 'MGXH1T2', 'MGXH2T2', 'MGXH1T3', 'MGXH2T3', 'MGDCGSZ', 'RIAGENDR']
    x = pd.DataFrame([int_features], columns=features);

    numiric_cols = ['BMXWT', 'BMXHT', 'BMXBMI', 'RIDAGEYR', 'MGXH1T1', 'MGXH2T1', 'MGXH1T2', 'MGXH2T2', 'MGXH1T3', 'MGXH2T3', 'MGDCGSZ']
    scaler = preprocessing.StandardScaler().fit(x[numiric_cols])
    x_scaled = scaler.transform(x[numiric_cols])
    x_scaled = pd.DataFrame(x_scaled, index=x.index, columns=x[numiric_cols].columns)
    x_scaled = pd.concat([x_scaled, x['RIAGENDR']], axis=1)
    x_scaled

    prediction = model.predict(x)
    output = prediction[0]
    print(output)

    return render_template('index.html', prediction_text='Percent with osteoporosis is {}'.format(output))
'''
#if __name__ == '__main__':
#   app.run(debug = True)