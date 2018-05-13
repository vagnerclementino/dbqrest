import flask
from flask_sqlalchemy import SQLAlchemy
from dbqrest import config

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__)
app.config.from_object(config.TestingConfig)
db = SQLAlchemy(app)
