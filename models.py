from datetime import datetime

from exts import db


class Doctor(db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


class PatientInfo(db.Model):
    __tablename__ = 'patientinfo'
    id = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    mobile = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200))
    job = db.Column(db.Integer)
    nation = db.Column(db.String(100))
    marital_status = db.Column(db.Boolean)
    emergencyContact = db.Column(db.String(100))
    createDate = db.Column(db.DateTime, default=datetime.now)
    updateDate = db.Column(db.DateTime, default=datetime.now)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
