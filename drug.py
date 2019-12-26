from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import pandas as pd
import numpy as np

app = Flask(__name__, static_url_path="/static")

@app.route('/drug', methods=['GET', 'POST'])
def find():
    data=[]
    if request.method == 'POST':
        data = pd.read_csv("drugsprice.csv")
        data=np.array(data)
        j=0
        for i in range(data.size[0]):
            if(request.form['text']==data[i][1]):
                j=i
                break;

    return(render_template('prescribedmedicin.html'),medname=data[i][1],quantity=10,storename="",mprice=data[i][4])