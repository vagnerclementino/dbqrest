from dbqrest.app import app, db
from flask_restless import APIManager
from dbqrest.model.Question import Question
from dbqrest.model.Choice import Choice

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
                       url_prefix='/api/v1')

    manager.create_api(Choice,
                       methods=['GET', 'POST'],
                       url_prefix='/api/v1')

    app.run()
