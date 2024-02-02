import json

from flask import Flask, session, g, redirect, url_for, jsonify
from flask_migrate import Migrate

import config
from exts import db
from models import Doctor

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/myinfo')
def myinfo():
    # patienttest = PatientInfo.query.filter_by(name='patienttest').first()
    patienttest = {
        'usrname': 'patienttest',
        'mobile': '13800000000',
        'address': "北京",
        'job': 1,
        'nation': 'han'
    }
    return jsonify(patienttest)
    # return 'myinfo'


if __name__ == '__main__':
    app.run()
