from cgi import print_environ
from csv import excel
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        username = request.form['Username']
        file = request.form['upload_file']
        
        print(file)
        print(type(file))
        print(file.split("."))

        if file.split(".")[-1] == "xlsx":
            data = pd.read_excel(file)
            return render_template('data.html', data = data.to_html(), Username = username)

        elif file.split(".")[-1] == "csv":
            data = pd.read_csv(file)
            return render_template('data.html', data = data.to_html(), Username = username)
        
        
    else:
        return render_template('index.html')

    
if __name__ == '__main__':
    app.run(debug=True)