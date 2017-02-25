import json

import flask

import settings
import database
import models

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html', widgets=models.Widget.query.all())


@app.route('/api/get_widgets', methods=['GET'])
def get_widgets():
    return flask.Response(
        json.dumps([widget.to_dict() for widget in models.Widget.query.all()]),
        mimetype='application/json')


@app.route('/api/create_widget', methods=['POST'])
def create_widget():
    name = flask.request.form['name']
    url = flask.request.form['url']
    for widget in models.Widget.query.filter_by(name=name).all():
        database.db_session.delete(widget)

    widget = models.Widget()
    widget.name = name
    widget.url = url
    database.db_session.add(widget)
    database.db_session.commit()

    return flask.Response(
        json.dumps({"ok": True}),
        mimetype='application/json')


if __name__ == '__main__':
    database.init_db()
    app.run(debug=settings.DEBUG, host='0.0.0.0', port=settings.PORT)
