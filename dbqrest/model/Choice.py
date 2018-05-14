#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dbqrest.app import db


# Create your Flask-SQLALchemy models as usual but with the following two
# (reasonable) restrictions:
#   1. They must have a primary key column of type sqlalchemy.Integer or
#      type sqlalchemy.Unicode.
#   2. They must have an __init__ method which accepts keyword arguments for
#      all columns (the constructor in flask.ext.sqlalchemy.SQLAlchemy.Model
#      supplies such a method, so you don't need to declare a new one).
class Choice(db.Model):


    __tablename__ = 'choices'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Unicode)
    answer = db.Column(db.String(1))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    question = db.relationship('Question',
                               backref=db.backref('choices', lazy='dynamic'
                                                  )
                               )
