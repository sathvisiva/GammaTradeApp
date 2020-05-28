import flask
from flask import request
import json
import csv 
from datetime import datetime
import os.path

app = flask.Flask(__name__)

@app.route('/api', methods=['GET','POST'])
def home():
    if request.method == "POST":
        file_exists = os.path.isfile('sample_order_store.csv')
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        pp=5
        dict=request.get_json()
        with open('sample_order_store.csv', mode='a',newline='') as outfile:
            writer = csv.DictWriter(outfile,fieldnames=dict.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(dict)
    
        return "Written to file"
    else:
        return "Get"

app.run()

