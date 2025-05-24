from odoo import api, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)

def update_detailed_type_after_load(cr, registry):
    _logger.info("🔁 Executant hook update_detailed_type_after_load...")
    
    env = api.Environment(cr, SUPERUSER_ID, {})

    try:
        templates = env['product.template'].search([('is_event_ticket', '=', True)])
        templates.write({'detailed_type': 'event'})
        _logger.info(f"✅ Actualitzats {len(templates)} productes com a 'event'")
    except Exception as e:
        _logger.error(f"❌ Error en update_detailed_type_after_load: {e}")

    print("✔️ Hook update_detailed_type_after_load executat correctament")
