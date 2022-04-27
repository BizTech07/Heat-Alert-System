import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Initilalizing flask
app = Flask(__name__)
train_model = pickle.load(open('train.pkl','rb'))

@app.route('/')
def app_home():
    return render_template('prediction.html')

@app.route('/predict', methods = ['POST'])
def predict():
    val_initial = [int(x) for x in request.form.values()]
    val_final = [np.array(val_initial)]
    prediction = train_model.predict(val_final)
    
    output = round(prediction[0] , 2)
    return render_template('prediction.html', prediction_text = 'The excess temperature of the panel would be:{}'.format(output))
    

@app.route('/predict_api', methods = ['GET'])
def predict_api():
    data = request.get_json(force=True)
    prediction = train_model.predict([np.array(list(data.values()))])
    
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug= True)
    
    
