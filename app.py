from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('heartattack.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@app.route("/predict", methods=['POST'])
def predict():
     if request.method == 'POST':
          age = float(request.form['age'])
          anamia=int(request.form['anaemia'])
          diabetes=int(request.form['diabetes'])
          blood_pressue=int(request.form['high_blood_pressure'])
          serum=float(request.form['serum_creatinine'])
          sex=int(request.form['sex'])
          smoking=int(request.form['smoking'])
          prediction=model.predict([[ age,anamia,diabetes,blood_pressue,serum,sex,smoking]])
          return render_template('index.html',prediction_text="your heart attack possibility is {} percent".format(prediction))

     else:
        return render_template('index.html')







if __name__=="__main__":
    app.run(debug=True,use_reloader=False)