from flask import Flask, render_template, request, jsonify, flash, redirect
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
 
app = Flask(__name__)
         
app.secret_key = "caircocoders-ednalan"
         
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
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
 
if __name__ == "__main__":
    app.run(debug=True)