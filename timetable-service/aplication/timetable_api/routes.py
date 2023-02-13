from flask import jsonify

from . import timetable_api_blueprint
from ..models import Timetable


@timetable_api_blueprint.route('/', methods=['GET'])
def timetables():
    timetables = []
    for row in Timetable.query.all():
        timetables.append(row.to_json())
    response = jsonify({'timetables': timetables})
    return response
