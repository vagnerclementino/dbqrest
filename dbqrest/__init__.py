
import flask
from flask_sqlalchemy import SQLAlchemy
from dbqrest.config import flask_app_config

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__)
app.config.from_object(flask_app_config.DevelopmentConfig)
db = SQLAlchemy(app)
