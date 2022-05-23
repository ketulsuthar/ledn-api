from flask_restx import Api
from flask import Blueprint

from .main.controller.health_controller import api as health_ns
from .main.controller.account_controller import api as account_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Ledn API',
    version='1.0',
    description='Ledn api for account and transaction'
)

api.add_namespace(health_ns, path='/health')
api.add_namespace(account_ns, path='/accounts')
