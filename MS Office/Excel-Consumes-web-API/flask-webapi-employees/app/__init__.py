from flask import Flask
from configs import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    app.config["JSON_SORT_KEYS"] = False

    # Database binding
    db.app = app
    db.init_app(app)

    # register blueprint
    from app.employees import empbp
    app.register_blueprint(empbp)

    return app
