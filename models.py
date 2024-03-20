from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from exts import db


class Doctor(db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


# 用户基本信息
class PatientInfo(db.Model):
    __tablename__ = 'patientinfo'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    doctor_id = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    idNumber = db.Column(db.String(100), primary_key=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    mobile = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200))
    job = db.Column(db.Integer)
    nation = db.Column(db.String(100))
    marital = db.Column(db.Boolean)
    emergencyContact = db.Column(db.String(100))
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# 疾病状况评估
class sheet1B(db.Model):
    __tablename__ = 'sheet1B'
    patientId = db.Column(db.Integer, primary_key=True, nullable=False)
    chronicDisease = db.Column(db.Integer, nullable=True)
    medicationNames = db.Column(db.String(100), nullable=True)
    medicationDuration = db.Column(db.Integer, nullable=True)
    recentInfectionStatus = db.Column(db.Integer, nullable=True)
    recentJointSurgery = db.Column(db.Boolean, nullable=True)
    cardiovascularFamilyHistory = db.Column(db.Boolean, nullable=True)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# 体格信息
class sheet2A(db.Model):
    __tablename__ = 'sheet2A'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    patientId = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Double, nullable=True)
    weight = db.Column(db.Double, nullable=True)
    waistline = db.Column(db.Double, nullable=True)
    restingHeartRate = db.Column(db.Integer, nullable=True)
    sbp = db.Column(db.Integer, nullable=True)
    dbp = db.Column(db.Integer, nullable=True)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# 生化指标信息
class sheet2B(db.Model):
    __tablename__ = 'sheet2B'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    patientId = db.Column(db.Integer, nullable=False)
    tc = db.Column(db.Double, nullable=True)
    tg = db.Column(db.Double, nullable=True)
    ldl = db.Column(db.Double, nullable=True)
    hdl = db.Column(db.Double, nullable=True)
    fpg = db.Column(db.Double, nullable=True)
    hba1c = db.Column(db.Double, nullable=True)
    scr = db.Column(db.Double, nullable=True)
    alb = db.Column(db.Double, nullable=True)
    ast = db.Column(db.Double, nullable=True)
    alt = db.Column(db.Double, nullable=True)
    sua = db.Column(db.Double, nullable=True)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# 颈动脉指标信息
class sheet2C(db.Model):
    __tablename__ = 'sheet2C'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    patientId = db.Column(db.Integer, nullable=False)
    leftlmt = db.Column(db.Double, nullable=True)
    rightlmt = db.Column(db.Double, nullable=True)
    carotidAtheroscleroticPlaque = db.Column(db.Double, nullable=True)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# ABI指标信息
class sheet2D(db.Model):
    __tablename__ = 'sheet2D'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    patientId = db.Column(db.Integer, nullable=False)
    leftAbi = db.Column(db.Double, nullable=True)
    rightAbi = db.Column(db.Double, nullable=True)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# 肝脏指标信息
class sheet2E(db.Model):
    __tablename__ = 'sheet2E'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    patientId = db.Column(db.Integer, nullable=False)
    lfap = db.Column(db.Double, nullable=True)
    lsm = db.Column(db.Double, nullable=True)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# 体格势能表
class sheet3(db.Model):
    __tablename__ = 'sheet3'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    patientId = db.Column(db.Integer, nullable=False)
    crfTestType = db.Column(db.String(100), nullable=True)
    vo2Max = db.Column(db.Double, nullable=True)
    dhgs = db.Column(db.Double, nullable=True)
    sitUpTest5 = db.Column(db.Integer, nullable=True)
    balanceTest30 = db.Column(db.String(100), nullable=True)
    balanceTest60 = db.Column(db.String(100), nullable=True)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# 运动处方
class sheet4A(db.Model):
    __tablename__ = 'sheet4'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    object = db.Column(db.String(100), nullable=False)
    restingHeartRate = db.Column(db.Integer, nullable=True)
    comorbidities = db.Column(db.String(100), nullable=True)
    aerobicAdaptationPrescription = db.Column(db.Integer, nullable=True)
    aerobicImprovementPrescription = db.Column(db.Integer, nullable=True)
    aerobicStablePrescription = db.Column(db.Integer, nullable=True)
    resistanceAdaptationPrescription = db.Column(db.Integer, nullable=True)
    resistanceImprovementPrescription = db.Column(db.Integer, nullable=True)
    resistanceStablePrescription = db.Column(db.Integer, nullable=True)
    preparationNote = db.Column(db.String(100), nullable=True)
    antidiabeticDrugNote = db.Column(db.String(100), nullable=True)
    dietNote = db.Column(db.String(100), nullable=True)
    unexpectedEventsNote = db.Column(db.String(100), nullable=True)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# 有氧运动处方定义
class sheet4B(db.Model):
    __tablename__ = 'sheet4B'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    patientId = db.Column(db.Integer, nullable=False)
    # startTime = db.Column(db.TIMESTAMP, nullable=False)
    # endTime = db.Column(db.TIMESTAMP, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    aerobicExerciseType = db.Column(db.String(100), nullable=False)
    warmUpType = db.Column(db.String(100), nullable=False)
    warmUpDuration = db.Column(db.Integer, nullable=False)
    heartRateLowerLimit = db.Column(db.Integer, nullable=False)
    heartRateUpperLimit = db.Column(db.Integer, nullable=False)
    exerciseDuration = db.Column(db.Integer, nullable=False)
    exerciseFrequency = db.Column(db.Integer, nullable=False)
    coolingDownType = db.Column(db.String(100), nullable=False)
    coolingDownDuration = db.Column(db.Integer, nullable=False)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


# 抗阻运动处方定义
class sheet4C(db.Model):
    __tablename__ = 'sheet4C'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    patientId = db.Column(db.Integer, nullable=False)
    # startTime = db.Column(db.TIMESTAMP, nullable=False)
    # endTime = db.Column(db.TIMESTAMP, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    resistanceExerciseType = db.Column(db.String(100), nullable=True)
    coreMusclesInvolved = db.Column(db.String(100), nullable=True)
    warmUpType = db.Column(db.String(100), nullable=False)
    warmUpDuration = db.Column(db.Integer, nullable=False)
    exercises = db.Column(db.String(100), nullable=False)
    intensity = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    groupNumber = db.Column(db.Integer, nullable=False)
    restTime = db.Column(db.Integer, nullable=False)
    exerciseFrequency = db.Column(db.Integer, nullable=False)
    coolingDownType = db.Column(db.String(100), nullable=False)
    coolingDownDuration = db.Column(db.Integer, nullable=False)
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class ExerciseRecord(db.Model):
    __tablename__ = 'ExerciseRecord'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)  # 记录的id，自增
    patientId = db.Column(db.Integer, nullable=False)  # 患者id
    exerciseId = db.Column(db.Integer, nullable=False)  # 处方的id
    completeness = db.Column(db.Integer, nullable=False)  # 运动的完成度
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)
