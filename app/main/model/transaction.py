from .. import db
from account import Account

class Transaction(db.Document):
    """ User Model for storing user account related details """
    account = db.ReferenceField(Account)
    amount = db.IntField(required=True)
    type = db.StringField(max_length=7)
    user_email = db.StringField(required=True, max_length=30)
    created_at = db.DateTimeField()


    def __repr__(self):
        return "<Account '{}'>".format(self.user_email)