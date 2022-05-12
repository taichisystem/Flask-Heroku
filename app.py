from flask import flask
from flask import request
import pandas as pd
import datetime as dt

data = pd.read_csv('data.csv', names=['s','e','m']).set_idex('m')

series = pd.Series(index=range(data.s.min(), dt.now().year))

for m in data.index:
    series.loc[data.loc[m].s:data.loc[m].e] = m

app = flask.Flask(__name__)

@app.route('/',method=['GET'])
def home():
    year = request.args['year']
    try:
        return series.loc[year]
    except KeyError:
        return f'Invalid input ({series.index.min()} - {series.index.max()})'