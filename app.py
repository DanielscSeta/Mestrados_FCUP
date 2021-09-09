# save this as app.py
from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd

app = Flask(__name__)

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})

cashtag_tab = ['sup','lol']

@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values ,data=cashtag_tab)


for i in range(0,(len(cashtag_tab)-1)) :
    var=cashtag_tab[i]
    @app.route('/<var>')
    def company(var):
        return render_template('simple.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')