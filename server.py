#!/usr/bin/env python2.7
from flask import Flask
import conf

from flask_wtf.csrf import CSRFProtect
from flask.ext.login import LoginManager

login_manager = LoginManager()

API_PORT = conf.API_PORT

csrf = CSRFProtect()


def create_app():
    from controllers import org, index
    app = Flask(__name__)
    login_manager.init_app(app)
    csrf.init_app(app)
    app.secret_key = conf.SECRET_KEY

    app.register_blueprint(org.org)
    app.register_blueprint(index.index)

    return app