from flask import Flask, render_template, request
import mysql.connector as mysql
import pandas as pd

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

# connection to the DB and creation of ID table
def connection_to_DB():
    conn = mysql.connect(option_files = 'connection.cfg')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS ID(nom VARCHAR(255) PRIMARY KEY, prenom VARCHAR(255))")
    return conn

def get_db_info():
    conn = connection_to_DB()
    post = conn.execute('SELECT * FROM ID').fetchall()
    conn.close()
    if post is None:
        abort(404)
    return post



def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: division par zéro!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    choix = request.form['operation']
    name = request.form['name']
    surname = request.form['surname']

    conn = connection_to_DB()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ID VALUES (%s, %s)", (name, surname))
    conn.commit()
    conn.close()

    if choix == "addition":
        result = addition(num1, num2)
        operation = "+"
    elif choix == "soustraction":
        result = soustraction(num1, num2)
        operation = "-"
    elif choix == "multiplication":
        result = multiplication(num1, num2)
        operation = "*"
    elif choix == "division":
        result = division(num1, num2)
        operation = "/"

    return render_template('result.html',name=name, surname=surname, num1=num1, num2=num2, operation=operation, result=result)

#@app.route('/tableau')
#def tableau():
#    conn = connection_to_DB()
#    cursor = conn.cursor()
#    cursor.execute("SELECT * FROM ID")
#    data = cursor.fetchall()
#    conn.close()
#    return render_template('tableau.html', data=data)

@app.route('/tableau')
def tableau():
    conn = connection_to_DB()
    query = "SELECT * FROM ID;"
    result_dataFrame = pd.read_sql(query,conn)
    result_dataFrame.to_html('templates/tableau.html')
    conn.close()
    return render_template('tableau.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
