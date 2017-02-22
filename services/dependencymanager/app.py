import json

import flask

import settings

app = flask.Flask(__name__)

@app.route('/get_existing_microservices', methods=['GET'])
def get_widgets():
    return flask.Response(
        json.dumps({
            'messageboard': {
                'internal_url': 'http://127.0.0.1:5001/',
                'public_url': 'http://127.0.0.1:5001/',
            },
            'dashboard': {
                'internal_url': 'http://127.0.0.1:5002/',
                'public_url': 'http://127.0.0.1:5002/',
            }
        }),
        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
