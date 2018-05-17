#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dbqrest import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dbqrest.model.Choice import Choice
from dbqrest.model.Question import Question

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
