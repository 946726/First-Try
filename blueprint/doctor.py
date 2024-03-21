from datetime import datetime
from sqlalchemy import or_
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import PatientInfo, sheet4B, sheet2B, sheet4A, sheet4C

bp = Blueprint('doctor', __name__, url_prefix='/')


@bp.route('/doctor/patient_info_all/<doctor_id>', methods=['GET'])
def patient_info_all(doctor_id):
    try:
        patients = PatientInfo.query.filter_by(doctor_id=doctor_id).all()
        patients_list = []
        for patient in patients:
            user_data = {
                'id': patient.id,
                'name': patient.name,
                'sex': patient.sex
            }
            patients_list.append(user_data)
        return jsonify(patients_list)
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('doctor/search_patient/<search_info>', methods=['GET'])
def search(search_info: str):
    try:
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
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('/doctor/patient_info_base/<patient_id>', methods=['GET'])
def patient_info_base(patient_id):
    try:
        patients = PatientInfo.query.filter_by(id=patient_id).all()
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
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('/doctor/patient_info_tc/<patient_id>')
def patient_info_tc(patient_id):
    try:
        tc_infos = sheet2B.query.filter_by(patientId=patient_id).all()
        if not tc_infos:
            return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
        else:
            # 创建一个名为 patient 的字典，包含患者信息
            tc_infos_list = []
            for tc_info in tc_infos:
                user_data = {
                    'tc': tc_info.tc,
                    'id': tc_info.id
                }
                tc_infos_list.append(user_data)
            return jsonify(tc_infos_list)
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('/doctor/patient_info_tg/<patient_id>')
def patient_info_tg(patient_id):
    try:
        tg_infos = sheet2B.query.filter_by(patientId=patient_id).all()
        if not tg_infos:
            return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
        else:
            # 创建一个名为 patient 的字典，包含患者信息
            tg_infos_list = []
            for tc_info in tg_infos:
                user_data = {
                    'tg': tc_info.tg,
                    'id': tc_info.id
                }
                tg_infos_list.append(user_data)
            return jsonify(tg_infos_list)
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('/doctor/patient_info_aerobicAdaptationPrescription/<patient_id>')
def patient_info_aa_prescription(patient_id):
    try:
        prescriptions_id = sheet4A.query.filter_by(id=patient_id).all()
        aa_prescription_id = prescriptions_id[0].aerobicAdaptationPrescription
        aa_prescription = sheet4B.query.filter_by(id=aa_prescription_id).all()
        if not aa_prescription:
            return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
        else:
            aa_prescription_data = {
                # "startTime": aa_prescription.startTime,
                # "endTime": aa_prescription.endTime
                "type": aa_prescription[0].type,
                "warmUpType": aa_prescription[0].warmUpType,
                "warmUpDuration": aa_prescription[0].warmUpDuration,
                "heartRateLowerLimit": aa_prescription[0].heartRateLowerLimit,
                "heartRateUpperLimit": aa_prescription[0].heartRateUpperLimit,
                "exerciseDuration": aa_prescription[0].exerciseDuration,
                "exerciseFrequency": aa_prescription[0].exerciseFrequency,
                "coolingDownType": aa_prescription[0].coolingDownType,
                "coolingDownDuration": aa_prescription[0].coolingDownDuration
            }
            return jsonify(aa_prescription_data)
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('/doctor/patient_info_aerobicImprovementPrescription/<patient_id>')
def patient_info_ai_prescription(patient_id):
    try:
        prescriptions_id = sheet4A.query.filter_by(id=patient_id).all()
        ai_prescription_id = prescriptions_id[0].aerobicImprovementPrescription
        ai_prescription = sheet4B.query.filter_by(id=ai_prescription_id).all()
        if not ai_prescription:
            return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
        else:
            ai_prescription_data = {
                # "startTime": aa_prescription.startTime,
                # "endTime": aa_prescription.endTime
                "type": ai_prescription[0].type,
                "warmUpType": ai_prescription[0].warmUpType,
                "warmUpDuration": ai_prescription[0].warmUpDuration,
                "heartRateLowerLimit": ai_prescription[0].heartRateLowerLimit,
                "heartRateUpperLimit": ai_prescription[0].heartRateUpperLimit,
                "exerciseDuration": ai_prescription[0].exerciseDuration,
                "exerciseFrequency": ai_prescription[0].exerciseFrequency,
                "coolingDownType": ai_prescription[0].coolingDownType,
                "coolingDownDuration": ai_prescription[0].coolingDownDuration
            }
            return jsonify(ai_prescription_data)
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('/doctor/patient_info_aerobicStablePrescription/<patient_id>')
def patient_info_as_prescription(patient_id):
    try:
        prescriptions_id = sheet4A.query.filter_by(id=patient_id).all()
        as_prescription_id = prescriptions_id[0].aerobicStablePrescription
        as_prescription = sheet4B.query.filter_by(id=as_prescription_id).all()
        if not as_prescription:
            return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
        else:
            as_prescription_data = {
                # "startTime": aa_prescription.startTime,
                # "endTime": aa_prescription.endTime
                "type": as_prescription[0].type,
                "warmUpType": as_prescription[0].warmUpType,
                "warmUpDuration": as_prescription[0].warmUpDuration,
                "heartRateLowerLimit": as_prescription[0].heartRateLowerLimit,
                "heartRateUpperLimit": as_prescription[0].heartRateUpperLimit,
                "exerciseDuration": as_prescription[0].exerciseDuration,
                "exerciseFrequency": as_prescription[0].exerciseFrequency,
                "coolingDownType": as_prescription[0].coolingDownType,
                "coolingDownDuration": as_prescription[0].coolingDownDuration
            }
            return jsonify(as_prescription_data)
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('/doctor/patient_info_resistanceAdaptationPrescription/<patient_id>')
def patient_info_ra_prescription(patient_id):
    try:
        prescriptions_id = sheet4A.query.filter_by(id=patient_id).all()
        ra_prescription_id = prescriptions_id[0].resistanceAdaptationPrescription
        ra_prescription = sheet4C.query.filter_by(id=ra_prescription_id).all()
        if not ra_prescription:
            return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
        else:
            ra_prescription_data = {
                # "startTime": aa_prescription.startTime,
                # "endTime": aa_prescription.endTime
                "resistanceExerciseType": ra_prescription[0].resistanceExerciseType,
                "coreMusclesInvolved": ra_prescription[0].coreMusclesInvolved,
                "warmUpType": ra_prescription[0].warmUpType,
                "warmUpDuration": ra_prescription[0].warmUpDuration,
                "exercises": ra_prescription[0].exercises,
                "intensity": ra_prescription[0].intensity,
                "number": ra_prescription[0].number,
                "groupNumber": ra_prescription[0].groupNumber,
                "restTime": ra_prescription[0].restTime,
                "exerciseFrequency": ra_prescription[0].exerciseFrequency,
                "coolingDownType": ra_prescription[0].coolingDownType,
                "coolingDownDuration": ra_prescription[0].coolingDownDuration
            }
            return jsonify(ra_prescription_data)
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('/doctor/patient_info_resistanceImprovementPrescription/<patient_id>')
def patient_info_ri_prescription(patient_id):
    try:
        prescriptions_id = sheet4A.query.filter_by(id=patient_id).all()
        ri_prescription_id = prescriptions_id[0].resistanceImprovementPrescription
        ri_prescription = sheet4C.query.filter_by(id=ri_prescription_id).all()
        if not ri_prescription:
            return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
        else:
            ri_prescription_data = {
                # "startTime": aa_prescription.startTime,
                # "endTime": aa_prescription.endTime
                "resistanceExerciseType": ri_prescription[0].resistanceExerciseType,
                "coreMusclesInvolved": ri_prescription[0].coreMusclesInvolved,
                "warmUpType": ri_prescription[0].warmUpType,
                "warmUpDuration": ri_prescription[0].warmUpDuration,
                "exercises": ri_prescription[0].exercises,
                "intensity": ri_prescription[0].intensity,
                "number": ri_prescription[0].number,
                "groupNumber": ri_prescription[0].groupNumber,
                "restTime": ri_prescription[0].restTime,
                "exerciseFrequency": ri_prescription[0].exerciseFrequency,
                "coolingDownType": ri_prescription[0].coolingDownType,
                "coolingDownDuration": ri_prescription[0].coolingDownDuration
            }
            return jsonify(ri_prescription_data)
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})


@bp.route('/doctor/patient_info_resistanceStablePrescription/<patient_id>')
def patient_info_rs_prescription(patient_id):
    try:
        prescriptions_id = sheet4A.query.filter_by(id=patient_id).all()
        rs_prescription_id = prescriptions_id[0].resistanceStablePrescription
        rs_prescription = sheet4C.query.filter_by(id=rs_prescription_id).all()
        if not rs_prescription:
            return jsonify({'code': '0', 'msg': '没有找到该患者信息'})
        else:
            rs_prescription_data = {
                # "startTime": aa_prescription.startTime,
                # "endTime": aa_prescription.endTime
                "resistanceExerciseType": rs_prescription[0].resistanceExerciseType,
                "coreMusclesInvolved": rs_prescription[0].coreMusclesInvolved,
                "warmUpType": rs_prescription[0].warmUpType,
                "warmUpDuration": rs_prescription[0].warmUpDuration,
                "exercises": rs_prescription[0].exercises,
                "intensity": rs_prescription[0].intensity,
                "number": rs_prescription[0].number,
                "groupNumber": rs_prescription[0].groupNumber,
                "restTime": rs_prescription[0].restTime,
                "exerciseFrequency": rs_prescription[0].exerciseFrequency,
                "coolingDownType": rs_prescription[0].coolingDownType,
                "coolingDownDuration": rs_prescription[0].coolingDownDuration
            }
            return jsonify(rs_prescription_data)
    except Exception as e:
        return jsonify({'code': '-1', 'msg': '查询过程中出现异常: {}'.format(str(e))})
