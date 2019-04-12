from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from datetime import datetime
from joblib import dump, load
from json import loads,dumps
import numpy as np
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


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
    weekday = dt.weekday()
    dayofyear = dt.timetuple().tm_yday
    week = dt.isocalendar()[1]
    hour = dt.hour
    

    filename = "district_"+district+".pkl"
    # weekday	dayofyear	week	hour
    array = np.array([[weekday,dayofyear,week,hour]])
    model = load("models/"+filename) 

    pred = model.predict(array)
    singlepred = list(pred[0])
    columns = ['Assault', 'Battery', 'Burglary', 'Concealed carry license violation', 'Crime sexual assault', 'Criminal damage', 'Criminal trespass', 'Deceptive practice', 'Gambling', 'Homicide', 'Human trafficking', 'Interference with public officer', 'Intimidation', 'Kidnapping', 'Liquor law violation', 'Motor vehicle theft', 'Narcotics', 'Non-criminal', 'Non-criminal (subject specified)', 'Obscenity', 'Offense involving children', 'Other narcotic violation', 'Other offense', 'Prostitution', 'Public indecency', 'Public peace violation', 'Robbery', 'Sex offense', 'Stalking', 'Theft', 'Weapons violation']
    resp = [{"name": name, "number": value} for name, value in zip(columns, singlepred)]
    resp = sorted(resp, key=lambda x : x["number"], reverse=True)
    return jsonify(resp)


if __name__ == '__main__':
    app.run()
