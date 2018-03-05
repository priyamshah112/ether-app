from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mailgun import MailGun

import os

# Initializing database and flask app
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mailgun = MailGun()
mailgun.init_app(app)

# Importing views
import analyseether.views
