#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dbqrest import db
from sqlalchemy.orm import validates

# Create your Flask-SQLALchemy models as usual but with the following two
# (reasonable) restrictions:
#   1. They must have a primary key column of type sqlalchemy.Integer or
#      type sqlalchemy.Unicode.
#   2. They must have an __init__ method which accepts keyword arguments for
#      all columns (the constructor in flask.ext.sqlalchemy.SQLAlchemy.Model
#      supplies such a method, so you don't need to declare a new one).
class Choice(db.Model):
    __tablename__ = 'choices'
    __table_args__ = {"schema": "dbqrest"}

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Unicode)
    answer = db.Column(db.String(1))
    question_id = db.Column(db.Integer,
                            db.ForeignKey('dbqrest.questions.id')
                            )
    question = db.relationship('Question',
                               backref=db.backref('choices', lazy='dynamic'
                                                  )
                               )

    @validates('answer')
    def validate_email(self, key, answer):
        assert answer in ('S', 'N')
        return answer
