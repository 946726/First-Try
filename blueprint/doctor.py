from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import PatientInfo

bp = Blueprint('doctor', __name__, url_prefix='/')


@bp.route('/new_patient', methods=['POST'])
def new_patient():
    f = request.json
    id = f.get('id')
    username = f.get('username')
    password = f.get('password')
    mobile = f.get('mobile')
    address = f.get('address')
    job = f.get('job')
    nation = f.get('nation')
    marital_status = f.get('marital_status')
    emergencyContact = f.get('emergencyContact')
    createDate = str(datetime.now())
    updateDate = str(datetime.now())
    # db.session.add(new_patient)
    # db.session.commit()
    new_patient_obj = {
        "id": id,
        "username": username,
        "password": password,
        "mobile": mobile,
        "address": address,
        "job": job,
        "nation": nation,
        "marital_status": marital_status,
        "emergencyContact": emergencyContact,
        "createDate": createDate,
        "updateDate": updateDate
    }
    return jsonify(new_patient_obj)


@bp.route('/patient_info_all', methods=['GET'])
@bp.route('/patient_info_all/<pa_id>', methods=['GET'])
def patient_info_all(pa_id=None):
    if pa_id is None:
        return "patient_info_all_peoples"
    else:
        patient = {
            'id': '10000000000000',
            'usrname': 'patienttest',
            'mobile': '13800000000',
            'address': "北京",
            'job': 1,
            'nation': 'han',
            'marital_status': 1,
            'emergencyContact': '13800000000',
            'createDate': '2023-2-2',
            'updateDate': '2023-2-2'
        }
        return jsonify(patient)
