from flask import Flask,render_template, request
import os
import pandas as pd
import numpy as np
import csv


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files["berkas"]
        if not os.path.isdir('static'):
            os.mkdir('static')
        global filepath
        filepath = os.path.join('static',file.filename)
        file.save(filepath)
        global data
        data = pd.read_csv(filepath, delimiter=";")
        global npFile
        npFile = data.values
        return render_template('data.html', data=data.to_html(index=False))
    return render_template('index.html')

@app.route('/hasil', methods=['GET', 'POST'])
def hasil():
    if request.method == 'POST':
        baris = int(request.form["baris"])
        hasil = 1
        kolom = data.shape[1]
        for i in range(kolom):
            hasil *= npFile[baris][i]
        # angka1 = npFile[baris][0]
        # angka2 = npFile[baris][1]
        
   
    return render_template('hasil.html', hasil1=data.to_html(index=False), hasil2 = baris, hasil3 = kolom,  hasil4 = hasil)



if __name__ == '__main__':
    app.run(debug=True)