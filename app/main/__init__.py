"""Api app"""
from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app():
    """
    Create flask app
    :return: flask app object
    """
    # app initiliazation
    server = Flask(__name__)

    db.init_app(server)
    # server.config['MONGO_URI'] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' \
    #                              + os.environ['MONGODB_PASSWORD'] + '@' \
    #                              + os.environ['MONGODB_HOSTNAME'] + ':' \
    #                              + os.environ['MONGODB_PORT'] + '/'\
    #                              + os.environ['MONGODB_DATABASE']
    return server