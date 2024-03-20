from datetime import datetime
from sqlalchemy import or_
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import PatientInfo

bp = Blueprint('doctor', __name__, url_prefix='/')



"""
    获取患者信息列表

    Args:
        pa_id (str): 患者ID

    Returns:
        dict: 患者信息，包含以下字段：
            - id (str): 患者ID
            - usrname (str): 患者姓名
            - mobile (str): 患者手机号
            - address (str): 患者地址
            - job (int): 患者职业
            - nation (str): 患者民族
            - marital_status (int): 患者婚姻状态
            - emergencyContact (str): 紧急联系人手机号
            - createDate (str): 患者创建日期
            - updateDate (str): 患者更新日期
    """


@bp.route('/doctor/patient_info_all', methods=['GET'])
def patient_info_all():
    doctor_id = request.args.get('doctor_id')
    patients = PatientInfo.query.filter_by(doctor_id).all()
    patients_list = []
    for patient in patients:
        user_data = {
            'id': patient.id,
            'name': patient.name,
            'sex': patient.sex
        }
        patients_list.append(user_data)
    return jsonify(patients_list)


@bp.route('/doctor/patient_info/by_id', methods=['GET'])
def patient_info_id():
    pa_id = request.args.get('id')
    patients = PatientInfo.query.filter_by(id=pa_id).all()
    if not patients:
        return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
    else:
        # 创建一个名为 patient 的字典，包含患者信息
        patients_list = []
        for patient in patients:
            user_data = {
                'name': patient.name,
                'mobile': patient.mobile,
                'idNumber': patient.idNumber
            }
            patients_list.append(user_data)
        return jsonify(patients_list)
        # 返回 patient 的 JSON 格式化结果
    # 返回 patient 的 JSON 格式化结果


@bp.route('doctor/search_patient', methods=['GET'])
def search():
    search_info = request.args.get('search_info')
    search_infos = PatientInfo.query.filter(or_(PatientInfo.idNumber == search_info,
                                               PatientInfo.name == search_info)).all()
    if not search_infos:
        return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
    else:
        searchinfos_list = []
        for patient in search_infos:
            user_data = {
                'id': patient.id,
                'name': patient.name,
                'sex': patient.sex
            }
            searchinfos_list.append(user_data)
        return jsonify(searchinfos_list)
