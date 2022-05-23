from flask_restx import Resource
from ..utils.dto import AccountDto
from ..service.account_service import get_accounts

api = AccountDto.api
_account = AccountDto.account

@api.route('/<email>')
@api.param('email', 'The User email address')
@api.response(404, 'account not found.')
class Account(Resource):
    @api.doc('get_account')
    @api.marshal_with(_account)
    def get(self, email):
        """
        Return status ok from server
        :return: OK
        """
        print(email)
        return get_accounts(email)