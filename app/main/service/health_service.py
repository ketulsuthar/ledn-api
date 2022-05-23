from flask import jsonify


def get_server_status():
    """
    Return server status
    :return: OK
    """
    return jsonify(
        {
            'status': 'OK1'
        }
    )