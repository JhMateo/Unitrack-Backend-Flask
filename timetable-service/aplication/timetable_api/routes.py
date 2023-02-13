from . import timetable_api_blueprint
from .. import db
from ..models import Timetable
from flask import jsonify, request


@timetable_api_blueprint.route('/', methods=['GET'])
def timetables():
    timetables = []
    for row in Timetable.query.all():
        timetables.append(row.to_json())
    response = jsonify({'timetables': timetables})
    return response
