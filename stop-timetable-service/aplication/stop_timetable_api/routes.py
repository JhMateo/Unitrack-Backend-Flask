from . import stop_timetable_api_blueprint
from .. import db
from ..models import StopTimetable
from flask import jsonify, request


@stop_timetable_api_blueprint.route('/<int:timetable_id>', methods=['GET'])
def stops_ids(timetable_id):
    stops = [row.to_json() for row in StopTimetable.query.filter_by(timetable_id=timetable_id).all()]

    response = jsonify({'stops': stops})
    return response
