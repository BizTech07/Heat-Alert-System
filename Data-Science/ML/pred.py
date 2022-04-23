import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Initilalizing flask
pred = Flask(__name__)
train_model = pickle.load(open('train.pkl','rb'))

@pred.route('/')
def pred_home():
    return render_template('prediction.html')

@pred.route('/predict', methods = ['POST'])
def predict():
    val_initial = [int(x) for x in request.form.values()]
    val_final = [np.array(val_initial)]
    prediction = train_model.predict(val_final)
    
    output = round(prediction[0] , 2)
    return render_template('prediction.html', prediction_text = 'Predicted Yield would be kwh:{}'.format(output))
    

@pred.route('/predict_api', methods = ['GET'])
def predict_api():
    data = request.get_json(force=True)
    prediction = train_model.predict([np.array(list(data.values()))])
    
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    pred.run(debug= True)
    
    
