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

def get_date_features(dt):
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
    date_features = [get_date_features(dt)]
    time_range = [dt]
    for _ in range(168):
        dt += delta
        date_features.append(get_date_features(dt))
        time_range.append(dt)
    return date_features,time_range

def load_model(number):
    filename = "district_"+number+".pkl"
    model = load("models/"+filename) 
    return model

def create_df(rows, time_range):
    columns = ['Assault', 'Battery', 'Burglary', 'Concealed carry license violation', 'Crime sexual assault', 'Criminal damage', 'Criminal trespass', 'Deceptive practice', 'Gambling', 'Homicide', 'Human trafficking', 'Interference with public officer', 'Intimidation', 'Kidnapping', 'Liquor law violation', 'Motor vehicle theft', 'Narcotics', 'Non-criminal', 'Non-criminal (subject specified)', 'Obscenity', 'Offense involving children', 'Other narcotic violation', 'Other offense', 'Prostitution', 'Public indecency', 'Public peace violation', 'Robbery', 'Sex offense', 'Stalking', 'Theft', 'Weapons violation']
    df = pd.DataFrame(rows, columns = columns, index=time_range)
    return df 

def get_model_prediction_for_district(number,dt):
    model = load_model(number)
    data_features,time_range = get_next_week(dt)
    predictions = model.predict(data_features)    
    df = create_df(predictions, time_range)
    # group by hour and day
    grouped_hour = df.resample('H').sum()
    agg_grouped_hour = grouped_hour.sum(axis=0).to_json(orient='records')
    grouped_hour = grouped_hour.to_json(orient='records')
    # grouped_hour = 
    grouped_day = df.resample('D').sum()
    agg_grouped_day = grouped_day.sum(axis=0).to_json(orient='records')
    grouped_day = grouped_day.to_json(orient='records')
    records = df.to_json(orient='records')
    return (grouped_hour, agg_grouped_hour, grouped_day, agg_grouped_day, records)

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
    grouped_hour, agg_grouped_hour, grouped_day, agg_grouped_day, records = get_model_prediction_for_district(district, dt)
    response = {
        "grouped_hour":grouped_hour, "agg_grouped_hour":agg_grouped_hour, "grouped_day":grouped_day, "agg_grouped_day":agg_grouped_day, "records":records,
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
