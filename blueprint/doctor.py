from datetime import datetime

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
    # 从请求的JSON数据中获取参数
    f = request.json
    # 获取id参数
    patientid = f.get('id')
    # 获取username参数
    username = f.get('username')
    # 获取password参数
    password = f.get('password')
    # 获取mobile参数
    mobile = f.get('mobile')
    # 获取address参数
    address = f.get('address')
    # 获取job参数
    job = f.get('job')
    # 获取nation参数
    nation = f.get('nation')
    # 获取marital_status参数
    marital_status = f.get('marital_status')
    # 获取emergencyContact参数
    emergencyContact = f.get('emergencyContact')
    # 获取当前时间并转换为字符串格式作为创建日期和更新日期
    createDate = str(datetime.now())
    updateDate = str(datetime.now())
    # 创建一个新的患者对象字典
    new_patient_obj = {
        "id": patientid,
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
@bp.route('/patient_info_all/<pa_id>', methods=['GET'])
def patient_info_all(pa_id=None):
    # 如果 pa_id 为 None，则返回 "patient_info_all_peoples"
    if pa_id is None:
        return "patient_info_all_peoples"
    else:
        # 创建一个名为 patient 的字典，包含患者信息
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
        # 返回 patient 的 JSON 格式化结果
        return jsonify(patient)
