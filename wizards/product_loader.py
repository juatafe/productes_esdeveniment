import base64
import json
from odoo import models, api
from odoo.modules.module import get_module_resource

class ProductLoader(models.TransientModel):
    _name = 'product.loader'
    _description = 'Importador de productes plantilla per a esdeveniments'

    @api.model
    def load_products(self):
<<<<<<< HEAD
        path = get_module_resource('productes_esdeveniment', 'data', 'productes.json')
=======
        path = get_module_resource('productes_esdeveniment', 'static', 'json', 'productes.json')
>>>>>>> 4491c27 (Initial import (neteja menús, event_views off, hooks fora))
        with open(path, 'r') as f:
            data = json.load(f)

        for item in data:
<<<<<<< HEAD
            image_path = get_module_resource('productes_esdeveniment', 'data', 'images', item['image_file'])
=======
            image_path = get_module_resource('productes_esdeveniment', 'static', 'img', item['image_file'])
>>>>>>> 4491c27 (Initial import (neteja menús, event_views off, hooks fora))
            with open(image_path, 'rb') as img:
                image_data = base64.b64encode(img.read())

            self.env['product.template'].create({
                'name': item['name'],
                'default_code': item['default_code'],
                'list_price': item['list_price'],
                'image_1920': image_data,
                'is_event_ticket': True,
                'type': 'product',
            })