import json
import logging
import time

import requests
import flask

import settings
import models
import database

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return flask.render_template('index.html', messages=models.Message.query.order_by('-id').all())


@app.route('/widgets/last_message_widget', methods=['GET'])
def last_message_widget():
    return flask.render_template('last_message_widget.html', last_message=models.Message.query.order_by('-id').first())


@app.route('/add_message/', methods=['GET', 'POST'])
def add_message():
    if flask.request.method == 'POST':
        message = models.Message()
        message.title = flask.request.form['title']
        message.content = flask.request.form['content']
        database.db_session.add(message)
        database.db_session.commit()
        return flask.render_template('add_message_ok.html')
    else:
        return flask.render_template('add_message.html')



def infinite_retry(callback):
    while True:
        try:
            result = callback()
            break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            logging.warn("Unable to get result, reconnecting...")
            pass
    return result


def register_widget():
    """Register our "view messages" widget with the "dashboard" microservice"""
    microservice_list = infinite_retry(lambda: requests.get(settings.MICROSERVICE_LIST_URL).json())
    def registration_routine():
        result = requests.post(
            microservice_list['dashboard']['internal_url'] + 'api/create_widget',
            {
                'name': 'Ostatnie ogłoszenie',
                'url': microservice_list['messageboard']['public_url'] + 'widgets/last_message_widget',
            }).json()
        assert result['ok'] == True

    infinite_retry(registration_routine)

if __name__ == '__main__':
    register_widget()
    app.run(debug=settings.DEBUG, host='0.0.0.0', port=settings.PORT)
