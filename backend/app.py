from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from datetime import datetime
from joblib import dump, load
from json import loads,dumps
import numpy as np
import pandas as pd
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

from datetime import datetime, timedelta

def get_times(dt):
    weekday = dt.weekday()
    dayofyear = dt.timetuple().tm_yday
    week = dt.isocalendar()[1]
    hour = dt.hour
    return (
        weekday, 
        dayofyear, 
        week, 
        hour, 
    )

def get_next_week(dt):
    delta = timedelta(hours=1)   
    time_range = [get_times(dt)]
    for _ in range(168):
        dt += delta
        time_range.append(get_times(dt))
    return time_range

def load_model(number):
    filename = "district_"+number+".pkl"
    model = load("models/"+filename) 
    return model

def create_df(rows):
    columns = ['Assault', 'Battery', 'Burglary', 'Concealed carry license violation', 'Crime sexual assault', 'Criminal damage', 'Criminal trespass', 'Deceptive practice', 'Gambling', 'Homicide', 'Human trafficking', 'Interference with public officer', 'Intimidation', 'Kidnapping', 'Liquor law violation', 'Motor vehicle theft', 'Narcotics', 'Non-criminal', 'Non-criminal (subject specified)', 'Obscenity', 'Offense involving children', 'Other narcotic violation', 'Other offense', 'Prostitution', 'Public indecency', 'Public peace violation', 'Robbery', 'Sex offense', 'Stalking', 'Theft', 'Weapons violation']
    df = pd.DataFrame(rows, columns = columns)
    return df 

def get_model_prediction_for_district(number,dt):
    model = load_model(number)
    time_ranges = get_next_week(dt)
    predictions = model.predict(time_ranges)    
    df = create_df(predictions)
    records = df.to_json(orient='records')
    return records

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api/1/models', methods=['GET'])
def models():
    time = request.args.get('time')
    date = request.args.get('date')
    district = request.args.get('district')
    datestring = date + ' ' + time
    dt = datetime.strptime(datestring, '%Y-%m-%d %H:%M')
    resp = get_model_prediction_for_district(district, dt)
    return jsonify(resp)


if __name__ == '__main__':
    app.run()
