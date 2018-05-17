#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dbqrest import db
from datetime import datetime

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

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True
                   )

    code = db.Column(db.Unicode(5),
                     nullable=False,
                     unique=True
                     )

    description = db.Column(db.Unicode(5000),
                            nullable=False
                            )

    creation_time = db.Column(db.DateTime,
                              nullable=False,
                              default=datetime.now()
                              )

    def __repr__(self):
        return '<Question: %s>' % self.description
