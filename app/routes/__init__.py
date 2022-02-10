from flask import Blueprint, Flask
from app.routes.vaccine_routes import bp as bp_vaccines

bp_api = Blueprint('api',__name__)

def init_app(app:Flask):
    bp_api.register_blueprint(bp_vaccines)

    app.register_blueprint(bp_api)