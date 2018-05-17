#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dbqrest import db


# Create your Flask-SQLALchemy models as usual but with the following two
# (reasonable) restrictions:
#   1. They must have a primary key column of type sqlalchemy.Integer or
#      type sqlalchemy.Unicode.
#   2. They must have an __init__ method which accepts keyword arguments for
#      all columns (the constructor in flask.ext.sqlalchemy.SQLAlchemy.Model
#      supplies such a method, so you don't need to declare a new one).
class Question(db.Model):
    __tablename__ = 'questions'
    __table_args__ = {"schema": "dbqrest"}

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Unicode, unique=True)
    description = db.Column(db.Unicode)

    def __repr__(self):
        return '<Question: %s>' % self.description
