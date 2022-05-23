from flask_restx import Resource
from ..utils.dto import HealthDto
from ..service.health_service import get_server_status

api = HealthDto.api


@api.route('/')
class Health(Resource):
    @api.doc('check_health')
    def get(self):
        """
        Return status ok from server
        :return: OK
        """
        return get_server_status()