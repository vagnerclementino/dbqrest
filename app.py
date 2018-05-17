from dbqrest import app, db
from flask_restless import APIManager
from dbqrest.model.Choice import Choice
from dbqrest.model.Question import Question
from dbqrest.config import constants

# start the flask loop
if __name__ == "__main__":

    # Create the database tables.
    db.create_all()
    # Create the Flask-Restless API manager.
    manager = APIManager(app, flask_sqlalchemy_db=db)

    # Create API endpoints, which will be available at /api/<tablename> by
    # default. Allowed HTTP methods can be specified as well.
    manager.create_api(Question,
                       methods=['GET', 'POST'],
                       url_prefix= constants.URL_PREFIX
                       )

    manager.create_api(Choice,
                       methods=['GET'],
                       url_prefix= constants.URL_PREFIX
                       )

    app.run()
