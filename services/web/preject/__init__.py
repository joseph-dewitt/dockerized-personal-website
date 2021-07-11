from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from preject.general import general_bp

app = Flask(__name__)
app.config.from_object("preject.config.Config")
db = SQLAlchemy(app)

app.register_blueprint(general_bp, url_prefix='/')


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email





# @app.route("/")
# def hello_world():
#     return jsonify(hello="world")


# @app.route("/static/<path:filename>")
# def staticfiles(filename):
#     return jsonify(hello=os.getenv('APP_FOLDER'))
