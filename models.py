from exts import db


class Doctor(db.Model):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.String(100), primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
