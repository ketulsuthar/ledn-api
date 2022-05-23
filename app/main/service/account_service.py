from flask import jsonify


def get_accounts(user_email):
    """
    Return server status
    :return: OK
    """
    return jsonify(
        {
            "first_name": 'test',
            "last_name": 'test',
            "balance": 5000,
            "country": 'CA',
            "email": user_email,
            "dob": '',
            "mfa": '',
            "referred_by": ''
        }
    )