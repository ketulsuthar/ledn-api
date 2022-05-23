from flask_restx import Namespace, fields


class HealthDto:
    api = Namespace('health', 'Check health for app')


class AccountDto:
    api = Namespace('account', 'Get user account')
    account = api.model('account', {
            'first_name': fields.String(required=True, description='user first name'),
            'last_name': fields.String(required=True, description='user last name'),
            'balance': fields.Integer(required=True, description='user balance'),
            'country': fields.String(required=True, description='user country'),
            'email': fields.String(required=True, description='user email'),
            'dob': fields.Date(required=True, description='user dob'),
            'mfa': fields.String(description='user mfa'),
            'referred_by': fields.String(description='user referred by'),
        })