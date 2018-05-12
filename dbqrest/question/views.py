from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from dbqrest import app, db
from dbqrest.question.models import Question

catalog = Blueprint('catalog', __name__)


@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."


class QuestionView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            questions = Question.query.paginate(page, 10).items
            res = {}
            for question in questions:
                res = {
                    'id': question.id,
                    'description': question.description
                }
        else:
            product = Question.query.filter_by(id=id).first()
            if not product:
                abort(404)

            res = {
                'id': question.id,
                'description': question.description
            }
        return jsonify(res)

    def post(self):
        desc_question = request.form.get('description')
        question = Question(desc_question)
        db.session.add(question)
        db.session.commit()
        return jsonify({question.id: {
            'description': question.description
        }})

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        # Delete the record for the provided id.
        return


question_view = QuestionView.as_view('question_view')
app.add_url_rule(
    '/question/', view_func=question_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/question/<int:id>', view_func=question_view, methods=['GET']
)
