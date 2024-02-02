from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import PatientInfo

bp = Blueprint('doctor', __name__, url_prefix='/')


@bp.route('/new_patient', methods=['POST'])
def new_patient():
    f = request.json
    # new_patient = PatientInfo()
    # new_patient.id = f.get('id')
    # new_patient.username = f.get('username')
    # new_patient.password = f.get('password')
    # new_patient.mobile = f.get('mobile')
    # new_patient.address = f.get('address')
    # new_patient.job = f.get('job')
    # new_patient.nation = f.get('nation')
    # new_patient.marital_status = f.get('marital_status')
    # new_patient.emergencyContact = f.get('emergencyContact')
    # new_patient.createDate = datetime.now
    # new_patient.updateDate = datetime.now
    # db.session.add(new_patient)
    # db.session.commit()
    return jsonify(f)


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
