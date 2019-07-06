from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://jim:12139@localhost/blog'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flaskblog import routes
