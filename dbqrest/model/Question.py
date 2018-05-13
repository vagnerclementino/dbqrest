#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dbqrest.app import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Unicode)

    def __repr__(self):
        return '<Question: %s>' % self.description
