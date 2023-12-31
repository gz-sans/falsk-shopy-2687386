#importacion o dependencias del proyecto
from flask import Flask
from config import Config
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)

#inicialiar el objeto sqlalchemy 
db = SQLAlchemy(app)
migrate = Migrate(app , db )



# entidades del proyecto
class Cliente(db.Model):
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True)