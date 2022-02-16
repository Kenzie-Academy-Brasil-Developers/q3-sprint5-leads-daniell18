from flask import Blueprint
from app.controllers import leads_controller
bp=Blueprint('',__name__,url_prefix='/leads')
bp.get('')(leads_controller.get_all)
bp.post('')(leads_controller.create)
bp.patch('')(leads_controller.update)
bp.delete('')(leads_controller.delete)