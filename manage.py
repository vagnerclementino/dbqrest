#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dbqrest import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
