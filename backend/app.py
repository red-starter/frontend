from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

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
    response_object = {'status': 'success'}

    time = request.args.get('time')
    date = request.args.get('date')
    district = request.args.get('district')
    print(request.args)
    response_object['model'] = 'hello'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
