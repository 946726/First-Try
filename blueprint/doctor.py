from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import PatientInfo


bp = Blueprint('doctor', __name__, url_prefix='/')


@bp.route('/new_patient', methods=['POST'])
def new_patient():
    f = request.json
    new_patient = PatientInfo()
    return "new_patient"


@bp.route('/patient_info_all/<pa_id>', methods=['GET'])
def patient_info_all(pa_id):
    if pa_id is None:
        return "patient_info_all_people"
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
