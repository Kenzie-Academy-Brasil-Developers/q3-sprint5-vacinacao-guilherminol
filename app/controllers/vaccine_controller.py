from http import HTTPStatus
from flask import jsonify, request
from app.models.vaccine_model import VaccineRecord
from sqlalchemy.exc import IntegrityError
from app.configs.database import db
import datetime

def get_all_logs():
    logs = (VaccineRecord.query.all())

    serialized_logs =[ {
        "cpf":  log.cpf,
        "name": log.name,
        "first shot date": log.first_shot_date,
        "second show date": log.second_shot_date,
        "vaccine name" : log.vaccine_name,
        "health unit name" : log.health_unit_name
    }for log in logs]

    return jsonify(serialized_logs),HTTPStatus.OK

def add_log():
    
    data = request.get_json()

    if not VaccineRecord.checkdata(data):
        return {"error": "there are values that are not strings"},HTTPStatus.BAD_REQUEST

    data = VaccineRecord.normalize(data)
    data["first_shot_date"] = datetime.datetime.now()
    data["second_shot_date"] = (datetime.datetime.now() + datetime.timedelta(days = 90))

    try:
        log = VaccineRecord(**data)

    except TypeError:
        return {"error": "Invalid keys"},HTTPStatus.BAD_REQUEST

    try:
        db.session.add(log)
        db.session.commit()

    except IntegrityError:
        return {"error": "CPF already exists"},HTTPStatus.CONFLICT

    return jsonify(log),HTTPStatus.CREATED