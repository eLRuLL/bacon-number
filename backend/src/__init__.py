from flask import Flask
from flask_cors import CORS


def create_app(config_filename='dev'):
    app = Flask(__name__)
    app.config.from_object('config')

    from src import db
    db.init_app(app)

    from src import api
    app.register_blueprint(api.bp)
    CORS(app)
    app.add_url_rule('/', endpoint='index')
    return app
