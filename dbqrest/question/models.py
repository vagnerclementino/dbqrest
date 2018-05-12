from dbqrest import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<Question: %s>' % self.description
