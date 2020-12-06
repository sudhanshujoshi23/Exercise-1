from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from exercise.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)

    from exercise.Fund.routes import funds
    from exercise.Investor.routes import investors
    from exercise.main.routes import main

    app.register_blueprint(funds)
    app.register_blueprint(investors)
    app.register_blueprint(main)

    return app

