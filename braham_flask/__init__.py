#!/usr/bin/env python
#
# http://flask.pocoo.org/docs/1.0/tutorial/factory/
#
import os

from flask import Flask
from . import db
from . import auth
from . import blog
from . import ame

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'braham_flask.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # initialize app
    db.init_app(app)

    # register auth blueprint
    app.register_blueprint(auth.bp)

    # register blog blueprint - index
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # register Acquirer's Multiple valutaion blueprint
    app.register_blueprint(ame.bp)

    return app
