import numpy as np

from flask import Flask, render_template, request, jsonify, flash, redirect
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
 
import pickle

app = Flask(__name__)


@app.route('/template')
def template():
    return render_template("template.html")


         
app.secret_key = "caircocoders-ednalan"
         
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'biztech07@4'
app.config['MYSQL_DB'] = 'biztech07'#----add the name of the data base here -  Biztech 7-----#
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
 
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM panelgeneration ORDER BY date")
    panelgeneration = cur.fetchall() 
    return render_template('index.html', panelgeneration=panelgeneration)#----connect the table--------#
  

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/chart')
def chart():
    return render_template("chart.html")

@app.route('/prediction')
def predi():
    return render_template("prediction.html")




@app.route("/range",methods=["POST","GET"])
def range(): 
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
    if request.method == 'POST':
        From = request.form['From']
        to = request.form['to']
        print(From)
        print(to)
        query = "SELECT * from panelgeneration WHERE date BETWEEN '{}' AND '{}'".format(From,to) #---------Change the sql query- add the correct table name----------#
        cur.execute(query)
        panelgenerationrange = cur.fetchall()#--------Check the range------------#
    return jsonify({'htmlresponse': render_template('response.html', panelgenerationrange=panelgenerationrange)})#----------set the range---------------#
 

train_model = pickle.load(open('Frontend/Project/src/trialRun/train.pkl','rb'))

@app.route('/')
def appShow():
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


info = {
    "Meta Data": {
        "1. Information": "Daily Temperature details (irrediance, high, low, ambient) and panelId",
        "2. Symbol": "",
        "3. Last Refreshed": "2021-06-19 12:48:55",
        "4. Output Size": "Compact",
        "5. Time Zone": "Sri Lanka"
    },
    "Time Series (Daily)": {
        "2021-06-19": {
            "1. dailyYeild": "464.2934",
            "2. high": "97.5860",
            "3. low": "35.5000",
            "4. ambient": "100.3600",
            "5. panelId": "26348999"
        },
        "2021-06-18": {
            "1. dailyYeild": "510.0100",
            "2. high": "100.1100",
            "3. low": "45.4200",
            "4. ambient": "100.8600",
            "5. panelId": "26348999"
        },
        "2021-06-15": {
            "1. dailyYeild": "410.5100",
            "2. high": "94.5300",
            "3. low": "34.0700",
            "4. ambient": "100.1300",
            "5. panelId": "26348999"
        },
        "2021-06-14": {
            "1. dailyYeild": "620.6500",
            "2. high": "95.0300",
            "3. low": "32.0000",
            "4. ambient": "101.4200",
            "5. panelId": "26348999"
        },
        "2021-06-13": {
            "1. dailyYeild": "600.7200",
            "2. high": "97.0100",
            "3. low": "89.5600",
            "4. ambient": "100.8500",
            "5. panelId": "26348999"        },
        "2021-06-12": {
            "1. dailyYeild": "590.1000",
            "2. high": "92.4493",
            "3. low": "82.7500",
            "4. ambient": "101.3100",
            "5. panelId": "26348999"
        },
        "2021-06-11": {
            "1. dailyYeild": "429.3700",
            "2. high": "101.5200",
            "3. low": "92.6700",
            "4. ambient": "101.0500",
            "5. panelId": "26348999"
        },
        "2021-06-08": {
            "1. dailyYeild": "630.0924",
            "2. high": "65.9500",
            "3. low": "30.5400",
            "4. ambient": "101.6300",
            "5. panelId": "26348999"
        },
        "2021-06-07": {
            "1. dailyYeild": "463.6500",
            "2. high": "78.6900",
            "3. low": "40.3800",
            "4. ambient": "100.8800",
            "5. panelId": "26348999"
        },
        "2021-06-06": {
            "1. dailyYeild": "570.4800",
            "2. high": "60.6000",
            "3. low": "35.9000",
            "4. ambient": "102.4900",
            "5. panelId": "26348999"
        },
        "2021-06-05": {
            "1. dailyYeild": "410.0000",
            "2. high": "62.3300",
            "3. low": "41.5300",
            "4. ambient": "102.1900",
            "5. panelId": "26348999"
        },
        "2021-06-04": {
            "1. dailyYeild": "400.2600",
            "2. high": "63.8600",
            "3. low": "40.8510",
            "4. ambient": "101.6700",
            "5. panelId": "26348999"
        },
        "2021-06-01": {
            "1. dailyYeild": "829.2798",
            "2. high": "62.8600",
            "3. low": "42.1700",
            "4. ambient": "100.7900",
            "5. panelId": "26348999"
        },
        "2021-05-31": {
            "1. dailyYeild": "949.2900",
            "2. high": "61.9900",
            "3. low": "47.6100",
            "4. ambient": "98.8400",
            "5. panelId": "26348999"
        },
        "2021-05-30": {
            "1. dailyYeild": "929.3100",
            "2. high": "63.2500",
            "3. low": "46.9100",
            "4. ambient": "50.9500",
            "5. panelId": "26348999"
        },
        "2021-05-29": {
            "1. dailyYeild": "409.8400",
            "2. high": "65.8800",
            "3. low": "42.2300",
            "4. ambient": "98.0100",
            "5. panelId": "26348999"
        },
        "2021-05-25": {
            "1. dailyYeild": "739.3000",
            "2. high": "62.9800",
            "3. low": "43.8600",
            "4. ambient": "98.3600",
            "5. panelId": "26348999"
        },
        "2021-05-24": {
            "1. dailyYeild": "839.7250",
            "2. high": "60.9400",
            "3. low": "42.8100",
            "4. ambient": "98.3100",
            "5. panelId": "26348999"
        },
        "2021-05-23": {
            "1. dailyYeild": "639.7100",
            "2. high": "64.7300",
            "3. low": "41.3200",
            "4. ambient": "98.6600",
            "5. panelId": "26348999"
        },
        "2021-05-22": {
            "1. dailyYeild": "729.6800",
            "2. high": "62.1700",
            "3. low": "42.2000",
            "4. ambient": "97.5000",
            "5. panelId": "26348999"
        },
        "2021-05-21": {
            "1. dailyYeild": "509.0000",
            "2. high": "63.0100",
            "3. low": "40.8000",
            "4. ambient": "97.6000",
            "5. panelId": "26348999"
        },
        "2021-05-18": {
            "1. dailyYeild": "829.0100",
            "2. high": "60.9300",
            "3. low": "37.0100",
            "4. ambient": "96.3600",
            "5. panelId": "26348999"
        },
        "2021-05-17": {
            "1. dailyYeild": "409.7600",
            "2. high": "64.5401",
            "3. low": "30.8300",
            "4. ambient": "96.1800",
            "5. panelId": "26348999"
        },
        "2021-05-16": {
            "1. dailyYeild": "309.3600",
            "2. high": "61.4000",
            "3. low": "36.6150",
            "4. ambient": "97.1500",
            "5. panelId": "26348999"
        },
        "2021-05-15": {
            "1. dailyYeild": "209.2400",
            "2. high": "62.8500",
            "3. low": "35.3400",
            "4. ambient": "97.3200",
            "5. panelId": "26348999"
        },
        "2021-05-14": {
            "1. dailyYeild": "509.9200",
            "2. high": "63.6900",
            "3. low": "32.3100",
            "4. ambient": "98.0300",
            "5. panelId": "26348999"
        },
        "2021-05-11": {
            "1. dailyYeild": "208.8000",
            "2. high": "60.8700",
            "3. low": "35.0400",
            "4. ambient": "97.7000",
            "5. panelId": "26348999"
        },
        "2021-05-10": {
            "1. dailyYeild": "309.4600",
            "2. high": "59.9500",
            "3. low": "42.0500",
            "4. ambient": "97.9100",
            "5. panelId": "26348999"
        },
        "2021-05-09": {
            "1. dailyYeild": "409.0100",
            "2. high": "60.9700",
            "3. low": "46.0500",
            "4. ambient": "96.9400",
            "5. panelId": "26348999"
        },
        "2021-05-08": {
            "1. dailyYeild": "509.8456",
            "2. high": "62.1600",
            "3. low": "42.0631",
            "4. ambient": "95.8100",
            "5. panelId": "26348999"
        },
        "2021-05-07": {
            "1. dailyYeild": "509.1700",
            "2. high": "61.7100",
            "3. low": "35.1000",
            "4. ambient": "96.2200",
            "5. panelId": "26348999"
        },
        "2021-05-04": {
            "1. dailyYeild": "509.3200",
            "2. high": "60.3700",
            "3. low": "42.9200",
            "4. ambient": "95.1600",
            "5. panelId": "26348999"
        },
        "2021-05-03": {
            "1. dailyYeild": "709.9600",
            "2. high": "78.9250",
            "3. low": "46.4500",
            "4. ambient": "94.0700",
            "5. panelId": "26348999"
        },
        "2021-05-02": {
            "1. dailyYeild": "769.9900",
            "2. high": "70.1700",
            "3. low": "42.1900",
            "4. ambient": "93.5100",
            "5. panelId": "26348999"
        },
        "2021-05-01": {
            "1. dailyYeild": "749.2100",
            "2. high": "63.2900",
            "3. low": "42.7900",
            "4. ambient": "95.0000",
            "5. panelId": "26348999"
        },
        "2021-04-30": {
            "1. dailyYeild": "849.3300",
            "2. high": "62.3964",
            "3. low": "40.1500",
            "4. ambient": "93.5200",
            "5. panelId": "26348999"
        },
        "2021-04-27": {
            "1. dailyYeild": "839.6000",
            "2. high": "63.9000",
            "3. low": "45.9100",
            "4. ambient": "95.8200",
            "5. panelId": "26348999"
        },
        "2021-04-26": {
            "1. dailyYeild": "849.5500",
            "2. high": "64.1500",
            "3. low": "43.1000",
            "4. ambient": "94.2600",
            "5. panelId": "26348999"
        },
        "2021-04-25": {
            "1. dailyYeild": "809.3000",
            "2. high": "63.3000",
            "3. low": "42.2800",
            "4. ambient": "92.3100",
            "5. panelId": "26348999"
        },
        "2021-04-24": {
            "1. dailyYeild": "849.2420",
            "2. high": "64.4700",
            "3. low": "42.4100",
            "4. ambient": "93.1200",
            "5. panelId": "26348999"
        },
        "2021-04-23": {
            "1. dailyYeild": "899.7436",
            "2. high": "62.2900",
            "3. low": "30.6300",
            "4. ambient": "95.3500",
            "5. panelId": "26348999"
        },
        "2021-04-20": {
            "1. dailyYeild": "939.9100",
            "2. high": "61.1100",
            "3. low": "32.0500",
            "4. ambient": "95.0000",
            "5. panelId": "26348999"
        },
        "2021-04-19": {
            "1. dailyYeild": "839.4400",
            "2. high": "60.0700",
            "3. low": "34.3400",
            "4. ambient": "96.1100",
            "5. panelId": "26348999"
        },
        "2021-04-18": {
            "1. dailyYeild": "829.2200",
            "2. high": "65.7200",
            "3. low": "60.5200",
            "4. ambient": "96.4400",
            "5. panelId": "26348999"
        },
        "2021-04-17": {
            "1. dailyYeild": "949.0000",
            "2. high": "62.5400",
            "3. low": "64.8800",
            "4. ambient": "96.0700",
            "5. panelId": "26348999"
        },
        "2021-04-16": {
            "1. dailyYeild": "939.0700",
            "2. high": "62.6600",
            "3. low": "67.4200",
            "4. ambient": "94.1700",
            "5. panelId": "26348999"
        },
        "2021-04-13": {
            "1. dailyYeild": "069.0500",
            "2. high": "63.1800",
            "3. low": "32.4400",
            "4. ambient": "93.0800",
            "5. panelId": "26348999"
        },
        "2021-04-12": {
            "1. dailyYeild": "929.4300",
            "2. high": "61.1600",
            "3. low": "36.4300",
            "4. ambient": "93.5800",
            "5. panelId": "26348999"
        },
        "2021-04-11": {
            "1. dailyYeild": "899.0100",
            "2. high": "62.2900",
            "3. low": "34.4800",
            "4. ambient": "91.8600",
            "5. panelId": "26348999"
        },
        "2021-04-10": {
            "1. dailyYeild": "929.3900",
            "2. high": "61.2800",
            "3. low": "34.6400",
            "4. ambient": "92.8800",
            "5. panelId": "26348999"
        },
        "2021-04-09": {
            "1. dailyYeild": "869.0400",
            "2. high": "60.1700",
            "3. low": "32.6200",
            "4. ambient": "90.7700",
            "5. panelId": "26348999"
        },
        "2021-04-06": {
            "1. dailyYeild": "929.4900",
            "2. high": "61.4600",
            "3. low": "30.4800",
            "4. ambient": "90.2300",
            "5. panelId": "26348999"
        },
        "2021-04-05": {
            "1. dailyYeild": "899.4350",
            "2. high": "60.0650",
            "3. low": "31.4000",
            "4. ambient": "92.3800",
            "5. panelId": "26348999"
        },
        "2021-04-04": {
            "1. dailyYeild": "968.8500",
            "2. high": "60.7600",
            "3. low": "32.7300",
            "4. ambient": "92.3300",
            "5. panelId": "26348999"
        },
        "2021-04-03": {
            "1. dailyYeild": "938.5750",
            "2. high": "61.0500",
            "3. low": "31.8900",
            "4. ambient": "89.7100",
            "5. panelId": "26348999"
        },
        "2021-04-02": {
            "1. dailyYeild": "969.4700",
            "2. high": "64.8800",
            "3. low": "30.5100",
            "4. ambient": "88.5200",
            "5. panelId": "26348999"
        },
        "2021-03-29": {
            "1. dailyYeild": "979.1800",
            "2. high": "64.2900",
            "3. low": "35.4000",
            "4. ambient": "91.2700",
            "5. panelId": "26348999"
        },
        "2021-03-28": {
            "1. dailyYeild": "928.8200",
            "2. high": "63.2300",
            "3. low": "32.8730",
            "4. ambient": "89.3900",
            "5. panelId": "26348999"
        },
        "2021-03-27": {
            "1. dailyYeild": "819.9400",
            "2. high": "60.1390",
            "3. low": "34.5100",
            "4. ambient": "89.4700",
            "5. panelId": "26348999"
        },
        "2021-03-26": {
            "1. dailyYeild": "859.6100",
            "2. high": "62.0000",
            "3. low": "32.4000",
            "4. ambient": "93.7800",
            "5. panelId": "26348999"
        },
        "2021-03-23": {
            "1. dailyYeild": "938.5000",
            "2. high": "64.4600",
            "3. low": "35.0800",
            "4. ambient": "87.1800",
            "5. panelId": "26348999"
        },
        "2021-03-22": {
            "1. dailyYeild": "929.2650",
            "2. high": "61.7500",
            "3. low": "31.6600",
            "4. ambient": "89.7900",
            "5. panelId": "26348999"
        },
        "2021-03-21": {
            "1. dailyYeild": "859.9300",
            "2. high": "62.0500",
            "3. low": "32.2100",
            "4. ambient": "92.4800",
            "5. panelId": "26348999"
        },
        "2021-03-20": {
            "1. dailyYeild": "929.0500",
            "2. high": "65.7700",
            "3. low": "31.0000",
            "4. ambient": "93.1300",
            "5. panelId": "26348999"
        },
        "2021-03-19": {
            "1. dailyYeild": "849.7400",
            "2. high": "61.9000",
            "3. low": "32.1100",
            "4. ambient": "92.8900",
            "5. panelId": "26348999"
        },
        "2021-03-16": {
            "1. dailyYeild": "829.6800",
            "2. high": "60.3800",
            "3. low": "34.9200",
            "4. ambient": "94.6000",
            "5. panelId": "26348999"
        },
        "2021-03-15": {
            "1. dailyYeild": "849.5300",
            "2. high": "62.5800",
            "3. low": "35.8300",
            "4. ambient": "94.1800",
            "5. panelId": "26348999"
        },
        "2021-03-14": {
            "1. dailyYeild": "929.1200",
            "2. high": "61.4100",
            "3. low": "32.5000",
            "4. ambient": "93.8500",
            "5. panelId": "26348999"
        },
        "2021-03-13": {
            "1. dailyYeild": "879.0000",
            "2. high": "62.2400",
            "3. low": "33.9700",
            "4. ambient": "94.4100",
            "5. panelId": "26348999"
        },
        "2021-03-12": {
            "1. dailyYeild": "919.5000",
            "2. high": "61.2100",
            "3. low": "32.0400",
            "4. ambient": "96.7700",
            "5. panelId": "26348999"
        },
        "2021-03-09": {
            "1. dailyYeild": "919.2900",
            "2. high": "60.5400",
            "3. low": "48.0000",
            "4. ambient": "96.5400",
            "5. panelId": "26348999"
        },
        "2021-03-08": {
            "1. dailyYeild": "849.2700",
            "2. high": "61.1000",
            "3. low": "42.7650",
            "4. ambient": "94.4300",
            "5. panelId": "26348999"
        },
        "2021-03-07": {
            "1. dailyYeild": "969.1600",
            "2. high": "62.9406",
            "3. low": "45.4300",
            "4. ambient": "93.8600",
            "5. panelId": "26348999"
        },
        "2021-03-06": {
            "1. dailyYeild": "728.3400",
            "2. high": "61.4900",
            "3. low": "43.9410",
            "4. ambient": "93.3200",
            "5. panelId": "26348999"
        },
        "2021-03-05": {
            "1. dailyYeild": "879.3400",
            "2. high": "62.2700",
            "3. low": "42.2600",
            "4. ambient": "93.6400",
            "5. panelId": "26348999"
        },
        "2021-03-02": {
            "1. dailyYeild": "729.5800",
            "2. high": "61.1500",
            "3. low": "40.8600",
            "4. ambient": "93.0500",
            "5. panelId": "26348999"
        },
        "2021-03-01": {
            "1. dailyYeild": "929.9900",
            "2. high": "60.5700",
            "3. low": "41.8400",
            "4. ambient": "92.8500",
            "5. panelId": "26348999"
        },
        "2021-02-28": {
            "1. dailyYeild": "729.8400",
            "2. high": "62.7050",
            "3. low": "40.6300",
            "4. ambient": "93.7700",
            "5. panelId": "26348999"
        },
        "2021-02-27": {
            "1. dailyYeild": "649.7400",
            "2. high": "60.8400",
            "3. low": "42.2000",
            "4. ambient": "94.2000",
            "5. panelId": "26348999"
        },
        "2021-02-26": {
            "1. dailyYeild": "929.4000",
            "2. high": "60.4500",
            "3. low": "42.2500",
            "4. ambient": "95.4200",
            "5. panelId": "26348999"
        },
        "2021-02-23": {
            "1. dailyYeild": "969.7500",
            "2. high": "62.0700",
            "3. low": "40.3600",
            "4. ambient": "94.0600",
            "5. panelId": "26348999"
        },
        "2021-02-22": {
            "1. dailyYeild": "919.0500",
            "2. high": "61.7300",
            "3. low": "42.3600",
            "4. ambient": "91.7300",
            "5. panelId": "26348999"
        },
        "2021-02-21": {
            "1. dailyYeild": "949.9800",
            "2. high": "64.3595",
            "3. low": "41.4900",
            "4. ambient": "91.4900",
            "5. panelId": "26348999"
        },
        "2021-02-20": {
            "1. dailyYeild": "829.4750",
            "2. high": "62.0600",
            "3. low": "40.0100",
            "4. ambient": "92.7200",
            "5. panelId": "26348999"
        },
        "2021-02-16": {
            "1. dailyYeild": "859.4500",
            "2. high": "61.5000",
            "3. low": "43.8000",
            "4. ambient": "92.0000",
            "5. panelId": "26348999"
        },
        "2021-02-15": {
            "1. dailyYeild": "929.2100",
            "2. high": "62.7200",
            "3. low": "35.6200",
            "4. ambient": "92.6600",
            "5. panelId": "26348999"
        },
        "2021-02-14": {
            "1. dailyYeild": "728.5100",
            "2. high": "62.9900",
            "3. low": "32.4100",
            "4. ambient": "90.8100",
            "5. panelId": "26348999"
        },
        "2021-02-13": {
            "1. dailyYeild": "608.9300",
            "2. high": "61.0000",
            "3. low": "37.8000",
            "4. ambient": "89.8300",
            "5. panelId": "26348999"
        },
        "2021-02-12": {
            "1. dailyYeild": "828.7350",
            "2. high": "60.7800",
            "3. low": "31.9295",
            "4. ambient": "89.1300",
            "5. panelId": "26348999"
        },
        "2021-02-09": {
            "1. dailyYeild": "918.3000",
            "2. high": "64.9300",
            "3. low": "30.8300",
            "4. ambient": "88.1800",
            "5. panelId": "26348999"
        },
        "2021-02-08": {
            "1. dailyYeild": "718.7100",
            "2. high": "63.8750",
            "3. low": "35.7600",
            "4. ambient": "85.0100",
            "5. panelId": "26348999"
        },
        "2021-02-07": {
            "1. dailyYeild": "619.4900",
            "2. high": "62.7700",
            "3. low": "40.2000",
            "4. ambient": "89.6100",
            "5. panelId": "26348999"
        },
        "2021-02-06": {
            "1. dailyYeild": "498.8900",
            "2. high": "63.4750",
            "3. low": "52.2500",
            "4. ambient": "91.3300",
            "5. panelId": "26348999"
        },
        "2021-02-05": {
            "1. dailyYeild": "899.5600",
            "2. high": "62.2400",
            "3. low": "52.0000",
            "4. ambient": "88.0000",
            "5. panelId": "26348999"
        },
        "2021-02-02": {
            "1. dailyYeild": "429.6400",
            "2. high": "62.9700",
            "3. low": "56.5000",
            "4. ambient": "91.7800",
            "5. panelId": "26348999"
        },
        "2021-02-01": {
            "1. dailyYeild": "609.7900",
            "2. high": "61.0700",
            "3. low": "53.5813",
            "4. ambient": "94.2600",
            "5. panelId": "26348999"
        },
        "2021-01-31": {
            "1. dailyYeild": "509.7500",
            "2. high": "60.4000",
            "3. low": "52.5100",
            "4. ambient": "95.0100",
            "5. panelId": "26348999"
        },
        "2021-01-30": {
            "1. dailyYeild": "529.3000",
            "2. high": "62.6600",
            "3. low": "51.1000",
            "4. ambient": "92.7400",
            "5. panelId": "26348999"
        },
        "2021-01-29": {
            "1. dailyYeild": "809.1400",
            "2. high": "63.4500",
            "3. low": "54.7200",
            "4. ambient": "93.9200",
            "5. panelId": "26348999"
        },
        "2021-01-26": {
            "1. dailyYeild": "829.1200",
            "2. high": "60.0600",
            "3. low": "50.5800",
            "4. ambient": "94.0600",
            "5. panelId": "26348999"
        }
    }
}

@app.route("/result")
def result():

    return render_template("chartindex.html")

@app.route('/get_info',methods=['GET'])
def get_info():
    
    return jsonify(info) # returning a JSON response


if __name__ == "__main__":
    app.run(debug=True)
