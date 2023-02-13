from . import stop_api_blueprint
from .. import db
from ..models import Stop
from flask import jsonify, request


@stop_api_blueprint.route('/', methods=['POST'])
def stops():
    id_stops = request.json['stops']
    print(id_stops)
    stops = [row.to_json() for row in Stop.query.filter(Stop.id.in_(id_stops)).all()]

    response = jsonify({'stops': stops})
    return response
