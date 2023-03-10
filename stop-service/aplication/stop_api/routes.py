from flask import jsonify, request

from . import stop_api_blueprint
from ..models import Stop


@stop_api_blueprint.route('/', methods=['POST'])
def stops():
    id_stops = request.json['stops']
    print(id_stops)
    stops = [row.to_json() for row in Stop.query.filter(Stop.id.in_(id_stops)).all()]

    response = jsonify({'stops': stops})
    return response
