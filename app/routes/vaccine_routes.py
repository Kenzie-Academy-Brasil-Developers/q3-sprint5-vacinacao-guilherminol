from flask import Blueprint
from app.controllers import vaccine_controller

bp = Blueprint("vaccines",__name__,url_prefix = "/vaccines")

bp.get('')(vaccine_controller.get_all_logs)
bp.post('')(vaccine_controller.add_log)