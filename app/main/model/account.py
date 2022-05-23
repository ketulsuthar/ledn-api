from .. import db


class Account(db.Document):
    """ User Model for storing user account related details """
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    balance = db.IntField(required=True)
    country = db.StringField(max_length=3)
    email = db.StringField(required=True, max_length=30)
    dob = db.DateTimeField(required=True)
    mfa = db.StringField(max_length=5)
    referred_by = db.StringField(max_length=30)
    created_at = db.DateTimeField()
    updated = db.DateTimeField()

    def __repr__(self):
        return "<Account '{} {}'>".format(self.first_name, self.last_name)