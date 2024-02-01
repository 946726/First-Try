from flask import Flask, session, g, redirect, url_for
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


if __name__ == '__main__':
    app.run()
