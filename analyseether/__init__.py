from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import os

# Initializing database and flask app
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

# Importing views
import analyseether.views
