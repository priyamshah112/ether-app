from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mailgun import MailGun
from analyseether.config import ProductionConfig


# Initializing database and flask app
app = Flask(__name__)
app.config.from_object(ProductionConfig)

# Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mailgun = MailGun()
mailgun.init_app(app)

# Importing views
import analyseether.views
