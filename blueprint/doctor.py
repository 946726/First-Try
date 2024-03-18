from datetime import datetime
from sqlalchemy import or_
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import PatientInfo

bp = Blueprint('doctor', __name__, url_prefix='/')


@bp.route('/new_patient', methods=['POST'])
def new_patient():
    """
    创建新患者记录--test

    Args:
        无

    Returns:
        dict: 新创建的患者对象
    """
    req_data = request.get_json()
    new_patient_obj = PatientInfo(
        name=req_data['name'],
        idNumber=req_data['idNumber'],
        mobile=req_data['mobile'],
        address=req_data['address']
    )
    # 返回新创建的患者对象的JSON格式数据
    return jsonify(new_patient_obj)


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


@bp.route('/patient_info_all', methods=['GET'])
def patient_info_all():
    patients = PatientInfo.query.all()
    patients_list = []
    for patient in patients:
        user_data = {
            'idNumber': patient.idNumber,
            'name': patient.name
        }
        patients_list.append(user_data)
    return jsonify(patients_list)


@bp.route('/patient_info/<pa_id>', methods=['GET'])
def patient_info_id(pa_id=None):
    patients = PatientInfo.query.filter_by(id=pa_id).all()
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


@bp.route('/search', methods=['GET'])
def search():
    searchinfo = request.args.get("searchinfo")
    searchinfos = PatientInfo.query.filter(or_(PatientInfo.idNumber.contains(searchinfo),
                                               PatientInfo.name.contains(searchinfo))).all()
    if searchinfos is None:
        return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
    else:
        searchinfos_list = []
        for patient in searchinfos:
            user_data = {
                'name': patient.name,
                'mobile': patient.mobile,
                'idNumber': patient.address
            }
            searchinfos_list.append(user_data)
        return jsonify(searchinfos_list)
