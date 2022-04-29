from flask import Flask

from .main.routes import main
from todoapp.extensions import mongo

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI']='mongodb+srv://hakimpogba:hakim101101@cluster0.bpmts.mongodb.net/Test?retryWrites=true&w=majority'

    mongo.init_app(app)

    app.register_blueprint(main)

    return app