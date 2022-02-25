from flask import Blueprint
from app.controllers import leads_controllers

bp = Blueprint("leads", __name__, url_prefix="/leads")

bp.post('')(leads_controllers.create_lead)
bp.get('')(leads_controllers.get_all_leads)
bp.patch('')(leads_controllers.update_lead)
bp.delete('')(leads_controllers.delete_lead)