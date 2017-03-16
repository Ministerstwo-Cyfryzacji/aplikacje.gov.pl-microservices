import json
import logging
import time
from urllib.parse import urljoin
import argparse

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


def register_widget(self_url, dashboard_url):
    """Register our "view messages" widget with the "dashboard" microservice"""
    widget_url = urljoin(self_url, 'widgets/last_message_widget')
    def registration_routine():
        result = requests.post(
            urljoin(dashboard_url, 'api/create_widget'),
            {
                'name': 'Ostatnie ogłoszenie',
                'url': widget_url,
            }).json()
        assert result['ok'] == True

    infinite_retry(registration_routine)
    app.logger.info("Registered widget {} on dashboard at {}.".format(widget_url, dashboard_url))


def resolve_service_name(service_list_url, name, type):
    service_list = infinite_retry(lambda: requests.get(service_list_url).json())
    return service_list[name][type]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Messageboard service server.')
    parser.add_argument('--self-public-url', default=settings.SELF_PUBLIC_URL, help='Public URL of this service')
    parser.add_argument('--dashboard-url', default=settings.DASHBOARD_URL, help='URL of dashboard')
    parser.add_argument('--service-list-url', default=settings.SERVICE_LIST_URL, help='URL of service list, which will be used for resolving addresses not passed explicitly')
    parser.add_argument('--port', type=int, default=settings.PORT, help="Port to listen on")
    args = parser.parse_args()

    database.init_db()
    register_widget(
        args.self_public_url or resolve_service_name(args.service_list_url, 'messageboard', 'public_url'),
        args.dashboard_url or resolve_service_name(args.service_list_url, 'dashboard', 'internal_url'),
    )
    app.run(debug=settings.DEBUG, host='0.0.0.0', port=args.port)
